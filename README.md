# ARIA Intake Pipeline
**InSync Tech Inc. — Railway Service**

Receives ElevenLabs post-call webhooks from the ARIA intake agent, extracts structured client data using Claude Haiku, generates a populated intake PDF, and delivers it to the InSync Tech inbox via Resend.

---

## Flow

```
Client calls intake number
  → ElevenLabs ARIA intake agent conducts interview (10–15 min)
  → Call ends → ElevenLabs fires post-call webhook to this service
  → HMAC verified
  → Transcript extracted
  → Claude Haiku extracts all intake form fields → JSON
  → ReportLab generates populated intake PDF
  → Resend delivers email to ian@insynctech.io with PDF attached
```

---

## Files

| File | Purpose |
|------|---------|
| `main.py` | FastAPI app — webhook endpoint, HMAC verification, pipeline orchestration |
| `extractor.py` | Claude Haiku field extraction — transcript → structured JSON |
| `pdf_generator.py` | ReportLab PDF generation — JSON → populated intake report |
| `email_sender.py` | Resend delivery — PDF + inline summary email |
| `requirements.txt` | Python dependencies |
| `Procfile` | Railway start command |
| `.env.example` | Required environment variables |

---

## Endpoints

| Method | Path | Description |
|--------|------|-------------|
| `GET`  | `/` | Health check |
| `POST` | `/intake-webhook` | ElevenLabs post-call webhook receiver |

---

## Environment Variables

Set all of these in Railway dashboard (never commit to git):

```
INTAKE_WEBHOOK_SECRET   — HMAC secret (generate fresh, store in ElevenLabs webhook config)
ANTHROPIC_API_KEY       — Same key as Mel pipeline
ELEVENLABS_API_KEY      — Same key as Mel pipeline
RESEND_API_KEY          — Same key as Mel pipeline
FROM_EMAIL              — intake@insynctech.io
INSYNC_INBOX            — ian@insynctech.io
```

---

## Deployment — Railway

1. Push this folder to a new GitHub repo (e.g. `insynctech-intake-pipeline`)
2. In Railway: New Project → Deploy from GitHub → select repo
3. Set all environment variables in Railway dashboard
4. Railway auto-detects `Procfile` and deploys

Your webhook URL will be:
```
https://your-railway-app.railway.app/intake-webhook
```

---

## ElevenLabs Configuration

In your ElevenLabs intake agent dashboard:

1. Go to **Settings → Post-call webhook**
2. Set URL to your Railway webhook endpoint
3. Set secret to match `INTAKE_WEBHOOK_SECRET`
4. Enable **Send transcript** and **Send conversation metadata**

---

## Local Testing

```bash
# Install dependencies
pip install -r requirements.txt

# Copy and fill env vars
cp .env.example .env

# Run locally
uvicorn main:app --reload --port 8001

# Test with curl
curl -X POST http://localhost:8001/intake-webhook \
  -H "Content-Type: application/json" \
  -d '{"conversation_id": "test_123", "transcript": [{"role": "agent", "message": "Hi, this is ARIA"}, {"role": "user", "message": "Hi, my business is Venice Barbershop"}]}'
```

---

## Adding to Existing Mel Railway Service

If you want to add this as a new route on the existing Mel service instead of a separate deployment, copy `extractor.py`, `pdf_generator.py`, and `email_sender.py` into the Mel project and add the `/intake-webhook` route to the existing `main.py`. Use a different `INTAKE_WEBHOOK_SECRET` env var so the two webhooks stay independent.

---

*InSync Tech Inc. — Venice, Florida — insynctech.io*
