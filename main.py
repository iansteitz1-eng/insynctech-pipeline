"""
InSync Tech — ARIA Intake Interview Pipeline
Railway Service

Flow:
  ElevenLabs post-call webhook
    → HMAC verification
    → transcript extraction
    → Claude Haiku field extraction (JSON)
    → PDF report generation
    → Resend email to InSync Tech inbox
"""

import os
import hmac
import hashlib
import json
import logging
from datetime import datetime
from fastapi import FastAPI, Request, HTTPException, BackgroundTasks
from fastapi.responses import JSONResponse
import httpx

from extractor import extract_fields
from pdf_generator import generate_intake_pdf
from email_sender import send_intake_email
from form_populator import generate_intake_form
from follow_up_engine import build_followup
from agent_config import resolve_agent
from sms_sender import send_followup_sms
from followup_email import send_followup_email
from aria_brain import get_aria_response, send_telegram_message

logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
log = logging.getLogger(__name__)

app = FastAPI(title="InSync Tech — ARIA Intake Pipeline")

WEBHOOK_SECRET = os.environ.get("INTAKE_WEBHOOK_SECRET", "")
ELEVENLABS_API_KEY = os.environ.get("ELEVENLABS_API_KEY", "")


# ─── HEALTH ──────────────────────────────────────────────────────────────────

@app.get("/")
def health():
    return {"status": "ok", "service": "aria-intake-pipeline"}



# ─── MASTER WEBHOOK ROUTER ───────────────────────────────────────────────────

@app.post("/webhook")
async def master_webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Single entry point for all ElevenLabs post-call webhooks.
    Routes by agent_id to the correct handler:
      - intake    → intake pipeline (form population + email)
      - followup  → follow-up engine (tiered SMS + email)
      - client    → future client-specific handlers
    """
    raw_body = await request.body()

    if WEBHOOK_SECRET:
        sig_header = request.headers.get("ElevenLabs-Signature", "")
        if not _verify_hmac(raw_body, sig_header):
            log.warning("HMAC verification failed on master webhook")
            raise HTTPException(status_code=401, detail="Invalid signature")

    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    agent_id       = payload.get("agent_id", "unknown")
    conversation_id = payload.get("conversation_id", "unknown")
    agent_config   = resolve_agent(agent_id)
    handler        = agent_config.get("handler", "followup")
    client_name    = agent_config.get("client", os.environ.get("DEFAULT_BUSINESS_NAME", "InSync Tech"))

    log.info(f"[{conversation_id}] Master webhook — agent: {agent_id} | handler: {handler} | client: {client_name}")

    transcript = _extract_transcript(payload)
    if not transcript or len(transcript.strip()) < 20:
        return JSONResponse({"status": "skipped", "reason": "no_transcript"})

    if handler == "intake":
        background_tasks.add_task(process_intake, transcript, {
            "conversation_id": conversation_id,
            "agent_id": agent_id,
            "call_duration": payload.get("call_duration_secs", 0),
            "call_timestamp": payload.get("start_time_unix_secs", ""),
            "received_at": __import__("datetime").datetime.utcnow().isoformat(),
        })
    else:
        background_tasks.add_task(
            process_followup, transcript, client_name, "ARIA", conversation_id
        )

    return JSONResponse({
        "status": "accepted",
        "conversation_id": conversation_id,
        "handler": handler,
        "client": client_name
    })


# ─── WEBHOOK ─────────────────────────────────────────────────────────────────

@app.post("/intake-webhook")
async def intake_webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Receives ElevenLabs post-call webhook for the intake agent.
    Verifies HMAC, extracts transcript, kicks off background processing.
    """
    raw_body = await request.body()

    # ── HMAC verification ────────────────────────────────────────────────────
    if WEBHOOK_SECRET:
        sig_header = request.headers.get("ElevenLabs-Signature", "")
        if not _verify_hmac(raw_body, sig_header):
            log.warning("HMAC verification failed — rejecting webhook")
            raise HTTPException(status_code=401, detail="Invalid signature")

    # ── Parse payload ────────────────────────────────────────────────────────
    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON payload")

    log.info(f"Intake webhook received — call_id: {payload.get('conversation_id', 'unknown')}")

    # ── Extract transcript ───────────────────────────────────────────────────
    transcript = _extract_transcript(payload)
    if not transcript or len(transcript.strip()) < 50:
        log.warning("Transcript too short or missing — skipping processing")
        return JSONResponse({"status": "skipped", "reason": "transcript_too_short"})

    # ── Metadata ─────────────────────────────────────────────────────────────
    metadata = {
        "conversation_id": payload.get("conversation_id", ""),
        "agent_id":        payload.get("agent_id", ""),
        "call_duration":   payload.get("call_duration_secs", 0),
        "call_timestamp":  payload.get("start_time_unix_secs", ""),
        "received_at":     datetime.utcnow().isoformat(),
    }

    # ── Background: extract → PDF → email ───────────────────────────────────
    background_tasks.add_task(process_intake, transcript, metadata)

    return JSONResponse({"status": "accepted", "conversation_id": metadata["conversation_id"]})


# ─── BACKGROUND PROCESSOR ────────────────────────────────────────────────────

async def process_intake(transcript: str, metadata: dict):
    """
    Full async pipeline:
      1. Haiku extracts structured fields from transcript → JSON
      2. PDF generated from JSON
      3. Resend delivers email to InSync Tech inbox
    """
    conversation_id = metadata.get("conversation_id", "unknown")
    log.info(f"[{conversation_id}] Starting intake processing pipeline")

    # Step 1 — Field extraction
    try:
        fields = await extract_fields(transcript)
        log.info(f"[{conversation_id}] Field extraction complete — business: {fields.get('business_legal_name', 'unknown')}")
    except Exception as e:
        log.error(f"[{conversation_id}] Field extraction failed: {e}")
        return

    # Step 2 — PDF summary generation
    try:
        pdf_bytes = generate_intake_pdf(fields, metadata)
        log.info(f"[{conversation_id}] Summary PDF generated — {len(pdf_bytes)} bytes")
    except Exception as e:
        log.error(f"[{conversation_id}] PDF generation failed: {e}")
        return

    # Step 3 — Populate intake form docx
    try:
        form_bytes = generate_intake_form(fields, metadata)
        log.info(f"[{conversation_id}] Intake form populated — {len(form_bytes)} bytes")
    except Exception as e:
        log.error(f"[{conversation_id}] Form population failed: {e}")
        return

    # Step 4 — Email delivery (summary PDF + populated form)
    try:
        business_name = fields.get("business_legal_name") or fields.get("dba_name") or "New Client"
        await send_intake_email(pdf_bytes, form_bytes, business_name, fields, metadata)
        log.info(f"[{conversation_id}] Email delivered — both attachments sent for: {business_name}")
    except Exception as e:
        log.error(f"[{conversation_id}] Email delivery failed: {e}")
        return

    log.info(f"[{conversation_id}] Intake pipeline complete ✓")




# ─── FOLLOW-UP WEBHOOK ───────────────────────────────────────────────────────

@app.post("/followup-webhook")
async def followup_webhook(request: Request, background_tasks: BackgroundTasks):
    """
    Universal post-call follow-up webhook.
    Fires after any ARIA conversation — Mel, intake agent, or sales line.
    Determines tier from what was collected and sends appropriate follow-up.
    """
    raw_body = await request.body()

    if WEBHOOK_SECRET:
        sig_header = request.headers.get("ElevenLabs-Signature", "")
        if not _verify_hmac(raw_body, sig_header):
            log.warning("HMAC verification failed on follow-up webhook")
            raise HTTPException(status_code=401, detail="Invalid signature")

    try:
        payload = json.loads(raw_body)
    except json.JSONDecodeError:
        raise HTTPException(status_code=400, detail="Invalid JSON")

    transcript = _extract_transcript(payload)
    if not transcript or len(transcript.strip()) < 20:
        return JSONResponse({"status": "skipped", "reason": "no_transcript"})

    # Pull agent metadata from payload
    agent_meta = payload.get("agent", {}) or {}
    business_name = (
        agent_meta.get("name")
        or payload.get("business_name")
        or os.environ.get("DEFAULT_BUSINESS_NAME", "InSync Tech")
    )
    agent_name = agent_meta.get("agent_name", "ARIA")
    conversation_id = payload.get("conversation_id", "unknown")

    log.info(f"[{conversation_id}] Follow-up webhook received for: {business_name}")
    background_tasks.add_task(process_followup, transcript, business_name, agent_name, conversation_id)
    return JSONResponse({"status": "accepted", "conversation_id": conversation_id})


async def process_followup(
    transcript: str,
    business_name: str,
    agent_name: str,
    conversation_id: str
):
    """
    Background follow-up pipeline:
      1. Extract caller data + assess tier
      2. Generate SMS and/or email content
      3. Send SMS via Twilio
      4. Send email via Resend (tiers 3-4 only)
    """
    log.info(f"[{conversation_id}] Starting follow-up pipeline")

    try:
        followup = await build_followup(transcript, business_name, agent_name)
    except Exception as e:
        log.error(f"[{conversation_id}] Follow-up engine failed: {e}")
        return

    tier  = followup.get("tier", 0)
    phone = followup.get("phone")
    email = followup.get("email_address")

    log.info(f"[{conversation_id}] Follow-up tier: {tier} | phone: {bool(phone)} | email: {bool(email)}")

    if tier == 0:
        log.info(f"[{conversation_id}] Tier 0 — no contact info collected, skipping")
        return

    # Send SMS
    if followup.get("send_sms") and phone:
        sms_result = send_followup_sms(phone, followup["sms_text"])
        log.info(f"[{conversation_id}] SMS result: {sms_result.get('status')} — {phone}")

    # Send email (tiers 3-4)
    if followup.get("send_email") and email:
        try:
            email_result = await send_followup_email(
                to_email=email,
                subject=followup["email_subject"],
                inner_html=followup["email_html"],
                business_name=business_name,
                tier=tier
            )
            log.info(f"[{conversation_id}] Email result: {email_result.get('status')} — {email}")
        except Exception as e:
            log.error(f"[{conversation_id}] Follow-up email failed: {e}")

    log.info(f"[{conversation_id}] Follow-up pipeline complete — tier {tier} ✓")


# ─── HELPERS ─────────────────────────────────────────────────────────────────

def _verify_hmac(body: bytes, signature_header: str) -> bool:
    """Verify ElevenLabs HMAC-SHA256 webhook signature."""
    if not signature_header:
        return False
    try:
        # ElevenLabs format: "t=timestamp,v1=hash"
        parts = dict(p.split("=", 1) for p in signature_header.split(","))
        timestamp = parts.get("t", "")
        provided_sig = parts.get("v1", "")
        signed_payload = f"{timestamp}.".encode() + body
        expected = hmac.new(
            WEBHOOK_SECRET.encode(),
            signed_payload,
            hashlib.sha256
        ).hexdigest()
        return hmac.compare_digest(expected, provided_sig)
    except Exception as e:
        log.error(f"HMAC verification error: {e}")
        return False


def _extract_transcript(payload: dict) -> str:
    """
    Pull the full transcript text from the ElevenLabs webhook payload.
    Handles both transcript array format and plain text format.
    """
    # Format 1: transcript as array of turn objects
    turns = payload.get("transcript", [])
    if isinstance(turns, list) and turns:
        lines = []
        for turn in turns:
            role = turn.get("role", "unknown").upper()
            text = turn.get("message", "").strip()
            if text:
                lines.append(f"{role}: {text}")
        return "\n".join(lines)

    # Format 2: concatenated_transcript string
    concat = payload.get("concatenated_transcript", "")
    if concat:
        return concat

    # Format 3: analysis summary fallback
    analysis = payload.get("analysis", {})
    summary = analysis.get("transcript_summary", "")
    if summary:
        return summary

    return ""


# ─── DATETIME TOOL (ElevenLabs Custom Tool) ──────────────────────────────────

from zoneinfo import ZoneInfo

@app.get("/tools/datetime")
def get_datetime():
    """
    Returns current date and time in Eastern time.
    Registered as a custom tool in ElevenLabs — called by Mel at conversation start.
    """
    now = datetime.now(ZoneInfo("America/New_York"))
    return {
        "day_of_week": now.strftime("%A"),
        "date": now.strftime("%B %d, %Y"),
        "time": now.strftime("%I:%M %p"),
        "full": now.strftime("%A, %B %d, %Y at %I:%M %p ET")
    }

# ─── TELEGRAM ────────────────────────────────────────────────────────────────
from aria_brain import get_aria_response, send_telegram_message

@app.post("/telegram")
async def telegram_webhook(request: Request, background_tasks: BackgroundTasks):
    try:
        data = await request.json()
    except Exception:
        return JSONResponse({"status": "bad_request"})
    message = data.get("message", {})
    if not message:
        return JSONResponse({"status": "no_message"})
    chat_id = message.get("chat", {}).get("id")
    text = message.get("text", "").strip()
    if not chat_id or not text:
        return JSONResponse({"status": "skipped"})
    if text == "/start":
        await send_telegram_message(chat_id, "Aria online. What do you need?")
        return JSONResponse({"status": "ok"})
    if text.startswith("/"):
        return JSONResponse({"status": "ignored"})
    background_tasks.add_task(_handle_telegram_message, chat_id, text)
    return JSONResponse({"status": "accepted"})

async def _handle_telegram_message(chat_id: int, text: str):
    reply = await get_aria_response(chat_id, text)
    await send_telegram_message(chat_id, reply)

@app.get("/telegram/register")
async def register_telegram_webhook(request: Request):
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    base_url = os.environ.get("RAILWAY_PUBLIC_DOMAIN", "")
    webhook_url = f"https://{base_url}/telegram"
    async with httpx.AsyncClient() as client:
        r = await client.post(f"https://api.telegram.org/bot{token}/setWebhook", json={"url": webhook_url, "drop_pending_updates": True})
    return r.json()

@app.on_event("startup")
async def startup_register_webhook():
    import httpx
    token = os.environ.get("TELEGRAM_BOT_TOKEN", "")
    webhook_url = "https://web-production-18ab8.up.railway.app/telegram"
    if token:
        try:
            async with httpx.AsyncClient(timeout=10) as client:
                r = await client.post(
                    f"https://api.telegram.org/bot{token}/setWebhook",
                    json={"url": webhook_url, "drop_pending_updates": False}
                )
                log.info(f"Webhook registration: {r.json()}")
        except Exception as e:
            log.error(f"Webhook registration failed: {e}")
