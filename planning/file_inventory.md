# File inventory — insynctech-pipeline

> Index of every non-trivial file in the repo and what it carries.

## Cabinet files
| File | Purpose |
|---|---|
| `AGENTS.md` | Router · first file every agent reads |
| `CLAUDE.md` | Thin builder adapter |
| `README.md` | Human overview (pre-Cabinet) |
| `docs/architecture.md` | Architecture + pipeline (VERIFICATION) |
| `docs/data_model.md` | Transient shapes (no DB) |
| `docs/api.md` | Webhook + health surface |
| `docs/permissions.md` | HMAC + env-key gating |
| `docs/validation.md` | Inbound + extraction + render validation |
| `planning/state.md` | LEARNING |
| `planning/decisions.md` | Append-only DECISION |
| `planning/domain.md` | InSync Tech context (VERIFICATION) |
| `planning/risks.md` | CORRECTION |
| `planning/questions.md` | Open questions |
| `planning/file_inventory.md` | This file |
| `sprints/sprint_001/requirements.md` | Sprint goal |
| `sprints/sprint_001/blueprint.md` | How |
| `sprints/sprint_001/acceptance_criteria.md` | Verification |
| `sprints/sprint_001/handoff.md` | DOCUMENTATION |

## Source files (flat — at repo root)
| File | Purpose |
|---|---|
| `main.py` | FastAPI app + webhook endpoint + HMAC + orchestration |
| `agent_config.py` | Per-agent configuration resolver |
| `aria_brain.py` | Aria conversational logic + Telegram integration |
| `extractor.py` | Claude Haiku field extraction (transcript → JSON) |
| `pdf_generator.py` | ReportLab summary PDF |
| `form_populator.py` | python-docx populated intake form |
| `email_sender.py` | Resend delivery of summary + form |
| `sms_sender.py` | Resend/SMS follow-up |
| `follow_up_engine.py` | Follow-up scheduling logic |
| `followup_email.py` | Follow-up email composer |

## Design-time templates (at root; not loaded at runtime)
| File | Purpose |
|---|---|
| `ARIA_Client_Intake_Form_v4.docx` | Master intake form layout (form_populator output mirrors this) |
| `ARIA_Intake_Form_Populated_Sample.docx` | Example of populated output |
| `ARIA_Intake_Interview_Script.docx` | Reference script for the ARIA voice agent |
| `ARIA_Intake_Summary_Sample.pdf` | Example of summary PDF output |
| `ARIA_Invoice_Template.docx` | Downstream invoice template |
| `ARIA_Service_Agreement_Template.docx` | Downstream contract template |
| `ARIA_Welcome_Packet.docx` | Downstream welcome packet |

## Build/config
| File | Purpose |
|---|---|
| `Procfile` | `web: uvicorn main:app --host 0.0.0.0 --port $PORT` |
| `nixpacks.toml` | Railway build config |
| `requirements.txt` | pip deps |
| `.env.example` | Required env vars (ELEVENLABS_WEBHOOK_SECRET, ANTHROPIC_API_KEY, RESEND_API_KEY, TELEGRAM_BOT_TOKEN, etc.) |
