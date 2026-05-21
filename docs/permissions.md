# Permissions — insynctech-pipeline

> **What this file is:** access gating rules. VERIFICATION (BIRDS-01).

## Inbound gating
- The webhook is gated by HMAC signature verification (ElevenLabs shared secret in `ELEVENLABS_WEBHOOK_SECRET`)
- The health endpoint is unauthenticated (Railway liveness probe)

## Outbound gating
- Resend API key (`RESEND_API_KEY`) — controls email send
- Anthropic API key (`ANTHROPIC_API_KEY`) — controls LLM calls
- Telegram bot token (`TELEGRAM_BOT_TOKEN`) — controls Aria brain DMs
- All keys are env-only; never committed; the `.env.example` enumerates them

## Where the gates live in code
- HMAC check: in `main.py` before dispatching the background task
- Outbound API auth: each sender module (`email_sender.py`, `extractor.py`, `aria_brain.py`) reads its key from env at module load

## Audit
This service does not maintain an audit log of its own. Resend + Anthropic + ElevenLabs each have their own delivery logs.
