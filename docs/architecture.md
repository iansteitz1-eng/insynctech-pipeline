# Architecture — insynctech-pipeline

> **What this file is:** durable technical truth about how the pipeline runs. VERIFICATION (BIRDS-01).

## Stack
- Python 3, FastAPI + uvicorn
- Anthropic SDK (Claude Haiku) for field extraction
- ReportLab for the summary PDF
- python-docx for the populated intake form
- Resend for outbound email + (optionally) SMS
- Telegram bot for follow-up loops
- Deploy: Railway (Procfile + nixpacks.toml)

## Repo layout (flat — see decisions.md re: src/ rename)
```
main.py              FastAPI app + webhook endpoint + orchestration
agent_config.py      Per-agent configuration resolver
aria_brain.py        Aria conversational logic + Telegram integration
extractor.py         Claude Haiku field extraction (transcript → JSON)
pdf_generator.py     ReportLab summary PDF
form_populator.py    python-docx populated intake form
email_sender.py      Resend delivery of summary + form
sms_sender.py        Resend/SMS follow-up
follow_up_engine.py  Follow-up scheduling logic
followup_email.py    Follow-up email composer
ARIA_*.docx/.pdf     Design-time reference templates (NOT loaded at runtime)
.env.example         Required environment variables
Procfile             Railway start command
nixpacks.toml        Railway build config
requirements.txt     pip deps
```

## Pipeline
```
ElevenLabs ARIA agent ends call
   ↓ post-call webhook
main.py: HMAC verify → extract transcript
   ↓
extractor.py (Claude Haiku): transcript → structured JSON
   ↓
pdf_generator.py: JSON → summary PDF
form_populator.py: JSON → populated intake form (.docx)
   ↓
email_sender.py: Resend → ian@insynctech.io with both attachments
   ↓ (optional)
follow_up_engine.py + sms_sender.py / followup_email.py: scheduled follow-ups
```

## Key boundaries
- HMAC verification is the gate — if it fails, drop the request before any LLM call.
- Extractor is the only LLM-touching module. All other modules are deterministic.
- Email delivery is the side-effect terminator. Anything past it is fire-and-forget.

## What this file is NOT
- A "best-practices" doc. Capture what's true of this codebase.
- A history. The git log is the history.
