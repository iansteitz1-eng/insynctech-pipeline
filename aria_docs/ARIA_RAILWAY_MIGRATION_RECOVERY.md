# ARIA RECOVERY & MIGRATION DOCUMENT
# InSync Tech, Inc. — April 4, 2026
# What happened, what was fixed, and how Aria now lives on Railway

---

## WHAT HAPPENED

Aria was running on KiloClaw (app.kilo.ai) — a cloud-hosted coding IDE. This was the wrong platform for a production AI assistant. KiloClaw is designed for writing code, not hosting a running AI brain. The consequences:

- **$400 in 4 days** — KiloClaw charges credits per LLM call. Loading 29 knowledge documents (587KB) into context on every single message burned credits at an unsustainable rate.
- **Telegram loop** — Aria got stuck in a message loop, processing and responding in cycles, burning credits exponentially.
- **Agent kept disappearing** — KiloClaw's Cloud Agent resets when sessions are dropped or context limits are hit. Every "information dump" into the chat killed the agent.
- **No persistence** — Sessions, agent configs, and knowledge were not durable. Every crash meant starting over.

**Root cause:** KiloClaw was never the right home. It has no flat-rate pricing, no webhook support, no persistent process, and no production infrastructure. Aria needed Railway.

---

## WHAT WAS BUILT

Aria now lives permanently on **Railway** — the same infrastructure that already runs the intake pipeline, ElevenLabs webhooks, and follow-up engine. Cost: pennies per day instead of $200 every 2 days.

### New Files Added to the Repo

**`aria_brain.py`** — Aria's brain module. Contains:
- A tight, efficient system prompt (~2KB) covering identity, products, team, pipeline, stack, and operating principles
- Claude Haiku as the LLM (fast, cheap, in-ecosystem)
- Per-user conversation history capped at 20 turns (controls token cost)
- `get_aria_response()` — handles all message processing
- `send_telegram_message()` — sends replies back to Telegram
- `register_webhook()` — auto-registers the Telegram webhook on every startup

**`aria_docs/`** — All 29 knowledge documents converted from `.txt` to `.md` and committed to the repo. These live on Railway's filesystem and are available for future on-demand retrieval (not loaded into context on every message).

### Routes Added to `main.py`

**`POST /telegram`** — Receives all incoming Telegram messages, routes to Aria brain in background, returns immediately so Telegram doesn't retry.

**`GET /telegram/register`** — Manual webhook registration endpoint (call once to set the webhook URL).

**`@app.on_event("startup")`** — Auto-registers the Telegram webhook every time Railway boots. This is what makes the setup permanent — no manual intervention needed after deploys.

---

## CURRENT ARCHITECTURE

```
Telegram (@AriaInSyncTechBot)
        ↓ webhook POST
Railway FastAPI (web-production-18ab8.up.railway.app)
        ↓ /telegram route
aria_brain.py → Claude Haiku API
        ↓ response
Telegram (message sent back to Ian)
```

**All existing functionality preserved:**
- ElevenLabs post-call webhooks (`/webhook`)
- Intake pipeline (`/intake-webhook`)
- Follow-up engine (`/followup-webhook`)
- Datetime tool for Mel (`/tools/datetime`)
- All 29 knowledge docs in `aria_docs/`

---

## TELEGRAM BOT

- **Bot:** @AriaInSyncTechBot
- **Token:** stored in Railway env var `TELEGRAM_BOT_TOKEN`
- **Webhook URL:** `https://web-production-18ab8.up.railway.app/telegram`
- **Auto-registers on startup:** Yes — never goes silent after a redeploy

---

## ENVIRONMENT VARIABLES (Railway — `celebrated-balance` project)

All existing vars preserved. One new var added:
- `TELEGRAM_BOT_TOKEN` — AriaInSyncTechBot token

---

## COST COMPARISON

| Platform | Cost | Stability |
|----------|------|-----------|
| KiloClaw (old) | ~$200 per 2 days | Drops agent on context overflow |
| Railway + Haiku (new) | ~$2-5/month | Permanent, auto-recovers |

Claude Haiku costs approximately $0.25 per million input tokens. A full month of active conversations with Aria will cost less than one KiloClaw credit purchase.

---

## WHAT ARIA KNOWS (System Prompt Summary)

Aria's core system prompt covers:
- Company identity and mission
- All 5 products (Aria, CertusOrdo, AnswrdBy.ai, PropertyFlow Pro, Symphony)
- Full team roster (Ian, John, Jarrett, Jim, key partners)
- Active sales pipeline with phone numbers and priorities
- Full tech stack
- Operating principles and response style

The 29 knowledge documents in `aria_docs/` are available for future on-demand retrieval and cover everything from sales playbooks to ROI calculators to the billion-dollar roadmap.

---

## WHAT'S NEXT

1. **Wire on-demand doc retrieval** — Aria should be able to pull any of the 29 docs when she needs them (e.g., "what does SALES_PLAYBOOKS say about dental offices?") without loading everything into context.
2. **Cancel KiloClaw** — No longer needed. Railway handles everything.
3. **Discord integration** — If needed, can be added as a new route on the same Railway service.
4. **Voice bridge rebuild** — ElevenLabs voice → Railway → Aria brain (previously lost in KiloClaw reset).

---

## RECOVERY COMMANDS (If Webhook Ever Goes Silent)

```bash
# Re-register webhook manually
curl "https://web-production-18ab8.up.railway.app/telegram/register"

# Check webhook status
curl "https://api.telegram.org/bot<TOKEN>/getWebhookInfo"

# Check Railway logs
cd ~/Desktop/insynctech-pipeline && railway logs --tail 50

# Redeploy
cd ~/Desktop/insynctech-pipeline && railway up
```

---

*Document generated April 4, 2026. Aria is live on Railway. She is stable.*
