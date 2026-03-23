"""
follow_up_engine.py
InSync Tech — Conversational Follow-Up Engine

Reads the call transcript and any collected caller data,
determines the appropriate follow-up tier, and generates
personalized content scaled to what was naturally collected.

Tier 1: Phone only             → warm thank you text
Tier 2: Phone + name + reason  → personalized text referencing call topic
Tier 3: Phone + email + biz    → text + email with ARIA overview one-pager
Tier 4: Full prospect call     → text + email with business-specific ROI summary PDF
"""

import os
import re
import json
import anthropic

ANTHROPIC_API_KEY = os.environ.get("ANTHROPIC_API_KEY", "")
client = anthropic.AsyncAnthropic(api_key=ANTHROPIC_API_KEY)

# ─── TIER ASSESSMENT ─────────────────────────────────────────────────────────

def assess_tier(caller_data: dict) -> int:
    """
    Determine follow-up tier based on what was naturally collected.
    Returns 1, 2, 3, or 4.
    """
    has_phone   = bool(caller_data.get("phone"))
    has_name    = bool(caller_data.get("name"))
    has_email   = bool(caller_data.get("email"))
    has_reason  = bool(caller_data.get("call_reason"))
    has_biz     = bool(caller_data.get("business_name") or caller_data.get("business_type"))
    has_details = bool(caller_data.get("pain_points") or caller_data.get("interest_level")
                       or caller_data.get("services_discussed"))

    if not has_phone:
        return 0  # nothing to send

    if has_email and has_biz and has_details:
        return 4  # full prospect — rich PDF
    if has_email and (has_biz or has_reason):
        return 3  # email + overview one-pager
    if has_name and has_reason:
        return 2  # warm personalized text
    return 1      # basic thank you text


# ─── HAIKU CALLER EXTRACTION ─────────────────────────────────────────────────

CALLER_EXTRACT_SYSTEM = """You are a data extraction assistant for InSync Tech.
Extract caller information from this call transcript.
Return ONLY valid JSON, no preamble or markdown."""

CALLER_EXTRACT_PROMPT = """Extract whatever the caller naturally shared during this conversation.
Only include fields that were actually mentioned — do not infer or fabricate.

Return a JSON object with these fields (use null if not mentioned):
{{
  "name": null,
  "phone": null,
  "email": null,
  "business_name": null,
  "business_type": null,
  "call_reason": null,
  "services_discussed": [],
  "pain_points": [],
  "interest_level": null,
  "follow_up_requested": false,
  "appointment_requested": false,
  "callback_requested": false,
  "key_topics": [],
  "caller_sentiment": null,
  "any_action_items": []
}}

TRANSCRIPT:
{transcript}"""


async def extract_caller_data(transcript: str) -> dict:
    """Extract what the caller naturally shared — name, phone, email, business context."""
    msg = await client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        system=CALLER_EXTRACT_SYSTEM,
        messages=[{"role": "user", "content": CALLER_EXTRACT_PROMPT.format(transcript=transcript)}]
    )
    raw = msg.content[0].text.strip()
    raw = re.sub(r"^```(?:json)?\s*", "", raw)
    raw = re.sub(r"\s*```$", "", raw)
    try:
        return json.loads(raw)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", raw, re.DOTALL)
        if match:
            return json.loads(match.group())
        return {}


# ─── CONTENT GENERATORS ──────────────────────────────────────────────────────

async def generate_sms_text(
    tier: int,
    caller_data: dict,
    business_name: str,
    agent_name: str = "ARIA"
) -> str:
    """Generate the SMS body for the given tier."""
    name       = caller_data.get("name", "")
    reason     = caller_data.get("call_reason", "")
    greeting   = f"Hi {name}" if name else "Hi there"

    if tier == 1:
        return (
            f"{greeting} — thank you for calling {business_name}. "
            f"We appreciate you reaching out. Don't hesitate to call anytime!"
        )

    if tier == 2:
        reason_ref = f" about {reason.lower()}" if reason else ""
        return (
            f"{greeting} — thanks for calling {business_name}{reason_ref}. "
            f"Hope to see you soon!"
        )

    if tier in (3, 4):
        return (
            f"{greeting} — thanks for your time on the call with {business_name} today. "
            f"We've sent some information to your email — check your inbox! "
            f"Feel free to reach out anytime."
        )

    return f"Thank you for calling {business_name}. We appreciate you reaching out!"


async def generate_email_subject(tier: int, caller_data: dict, business_name: str) -> str:
    """Generate email subject line."""
    name = caller_data.get("name", "")
    name_part = f", {name}" if name else ""

    if tier == 3:
        return f"Thanks for connecting{name_part} — InSync Tech / {business_name}"
    if tier == 4:
        biz = caller_data.get("business_name", "your business")
        return f"Your personalized ARIA overview — {biz} — InSync Tech"
    return f"Thanks for reaching out — {business_name}"


# ─── HAIKU SUMMARY GENERATORS ─────────────────────────────────────────────────

SUMMARY_SYSTEM = """You are a professional business writer for InSync Tech, an AI voice receptionist company.
Write in a warm, direct, and professional tone.
No fluff. No corporate buzzwords. Sound like a smart human who genuinely cares.
Return clean HTML suitable for an email body — no full HTML document wrapper, just the inner content."""


async def generate_tier3_email_html(
    caller_data: dict,
    business_name: str,
    agent_name: str
) -> str:
    """
    Tier 3: ARIA overview one-pager.
    Tailored to their business type and call reason.
    """
    biz_type = caller_data.get("business_type", "your business")
    reason   = caller_data.get("call_reason", "")
    topics   = caller_data.get("key_topics", [])
    name     = caller_data.get("name", "")

    prompt = f"""Write a professional follow-up email body for InSync Tech to send after a call.

Context:
- Caller name: {name or "not provided"}
- Their business type: {biz_type}
- What they called about: {reason or "general inquiry"}
- Key topics discussed: {", ".join(topics) if topics else "not captured"}
- Our product: ARIA, an AI voice receptionist that answers calls, transcribes, summarizes, and delivers post-call reports
- Business sending this: {business_name}

Write an email that:
1. Opens with a warm, genuine thank you (2-3 sentences max)
2. Has a section called "What ARIA Does for [biz_type] Businesses" — 3-4 specific, concrete bullet points tailored to their industry
3. Has a section called "What Happens on Every Call" — brief, 3 bullet points covering answer → summarize → deliver
4. Has a section called "Getting Started" — 2-3 sentences, keep it simple and approachable, no pressure
5. Closes with a personal sign-off from the InSync Tech team

Keep the tone conversational and genuine. No corporate speak.
Format as clean HTML with inline styles. Use #1A3D6B for headings, #404040 for body text.
No full HTML document wrapper — just the content div."""

    msg = await client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=2048,
        system=SUMMARY_SYSTEM,
        messages=[{"role": "user", "content": prompt}]
    )
    return msg.content[0].text.strip()


async def generate_tier4_email_html(
    caller_data: dict,
    business_name: str,
    agent_name: str
) -> str:
    """
    Tier 4: Full business-specific ROI summary.
    Uses everything the caller shared to build a personalized case.
    """
    biz_name   = caller_data.get("business_name", "your business")
    biz_type   = caller_data.get("business_type", "your business")
    pain_points= caller_data.get("pain_points", [])
    services   = caller_data.get("services_discussed", [])
    topics     = caller_data.get("key_topics", [])
    name       = caller_data.get("name", "")
    action_items = caller_data.get("any_action_items", [])

    prompt = f"""Write a personalized business summary email for InSync Tech to send after a prospect call.

Caller details naturally shared during the conversation:
- Name: {name or "not captured"}
- Business name: {biz_name}
- Business type: {biz_type}
- Pain points mentioned: {", ".join(pain_points) if pain_points else "not captured"}
- Topics discussed: {", ".join(services + topics) if (services or topics) else "not captured"}
- Action items from call: {", ".join(action_items) if action_items else "none noted"}

Our product: ARIA — an AI voice receptionist that answers every inbound call, identifies itself as AI,
captures caller info, transcribes the conversation, generates a summary, and delivers a post-call
report with MP3 recording to the business owner's inbox. $99/month, no contracts.

Write an email that:
1. Opens with a warm, specific thank you that references their actual business/situation (2-3 sentences)
2. Section: "What We Heard" — briefly reflects back the key things they shared (1-2 sentences, make them feel heard)
3. Section: "What ARIA Would Do for {biz_name}" — 4-5 SPECIFIC bullet points tailored to their exact business type and pain points. Be concrete. Not generic.
4. Section: "The Numbers" — a simple ROI table or paragraph showing time/cost saved. Use realistic estimates for their business type (e.g. if barbershop: avg 15 calls/day x 2 min x $X/hr = Y hours/month saved)
5. Section: "Next Steps" — simple, 3 steps, no pressure. Step 1: review this email. Step 2: call or reply with questions. Step 3: sign up takes 5 minutes.
6. Close with a genuine personal sign-off

Tone: Smart, direct, warm. Like a knowledgeable friend who runs a tech company.
No corporate speak. No hype. Real numbers. Specific to them.
Format as clean HTML with inline styles. #1A3D6B for headings, #404040 for body text, #2E75B6 for accents.
No full HTML wrapper — just the content div."""

    msg = await client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=3000,
        system=SUMMARY_SYSTEM,
        messages=[{"role": "user", "content": prompt}]
    )
    return msg.content[0].text.strip()


# ─── MASTER ORCHESTRATOR ─────────────────────────────────────────────────────

async def build_followup(
    transcript: str,
    business_name: str,
    agent_name: str = "ARIA",
    pre_extracted: dict = None
) -> dict:
    """
    Master function. Takes a transcript, returns everything needed to send the follow-up.

    Returns:
    {
        "tier": int,
        "caller_data": dict,
        "sms_text": str or None,
        "email_subject": str or None,
        "email_html": str or None,
        "send_sms": bool,
        "send_email": bool,
        "phone": str or None,
        "email": str or None,
    }
    """
    # Use pre-extracted caller data if available (from Mel pipeline), else extract fresh
    caller_data = pre_extracted if pre_extracted else await extract_caller_data(transcript)

    tier = assess_tier(caller_data)

    result = {
        "tier":          tier,
        "caller_data":   caller_data,
        "sms_text":      None,
        "email_subject": None,
        "email_html":    None,
        "send_sms":      False,
        "send_email":    False,
        "phone":         caller_data.get("phone"),
        "email_address": caller_data.get("email"),
    }

    if tier == 0:
        return result  # nothing to send

    # SMS for all tiers 1-4
    result["sms_text"] = await generate_sms_text(tier, caller_data, business_name, agent_name)
    result["send_sms"] = bool(result["phone"])

    # Email for tiers 3-4 only
    if tier >= 3 and result["email_address"]:
        result["email_subject"] = await generate_email_subject(tier, caller_data, business_name)

        if tier == 3:
            result["email_html"] = await generate_tier3_email_html(
                caller_data, business_name, agent_name
            )
        else:
            result["email_html"] = await generate_tier4_email_html(
                caller_data, business_name, agent_name
            )

        result["send_email"] = True

    return result
