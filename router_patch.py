import re

with open("main.py", "r") as f:
    content = f.read()

master_route = '''
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

'''

# Insert before the intake webhook route
content = content.replace(
    "# ─── WEBHOOK ───────────────────────────────────────────────────────────────",
    master_route + "\n# ─── WEBHOOK ───────────────────────────────────────────────────────────────"
)

# Add import for resolve_agent
content = content.replace(
    "from follow_up_engine import build_followup",
    "from follow_up_engine import build_followup\nfrom agent_config import resolve_agent"
)

with open("main.py", "w") as f:
    f.write(content)

print("Done" if "master_webhook" in content else "FAILED")
