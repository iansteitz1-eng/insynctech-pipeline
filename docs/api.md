# Public API — insynctech-pipeline

> **What this file is:** the HTTP surface this service exposes. VERIFICATION (BIRDS-01).

## Base URL
- Prod: Railway-assigned (see `RAILWAY_PUBLIC_DOMAIN` env)
- Local: `http://127.0.0.1:8000`

## Endpoints
*(See `main.py` for definitive list. Summary here for substrate orientation.)*

### `POST /webhook/elevenlabs/post-call`
- **Purpose:** Receive ElevenLabs post-call webhook for the ARIA intake agent
- **Auth:** HMAC signature in header, verified against `ELEVENLABS_WEBHOOK_SECRET` env
- **Body:** ElevenLabs post-call payload (transcript + metadata)
- **On success:** triggers extraction → PDF/DOCX → email pipeline (background task), returns 200 immediately
- **On HMAC failure:** returns 401 without invoking LLM

### `GET /health`
- **Purpose:** Liveness probe for Railway
- **Auth:** none
- **Response:** `{"status": "ok"}`

### Aria brain endpoints
- See `aria_brain.py` and `main.py` for the Telegram/Aria integration surface (separate from intake webhook)

## What's NOT public
- The internal extractor / generator modules are not exposed over HTTP. Only the webhook + health surface.
