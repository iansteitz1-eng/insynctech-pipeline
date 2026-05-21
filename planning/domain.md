# Domain — insynctech-pipeline (ARIA Intake Pipeline)

> **BIRDS-01 (VERIFICATION)** — the client's world in their words. NOT a tech description.

## Who is the user?

- **Primary user:** Ian Steitz (InSync Tech) — receives the intake summary in his inbox after every ARIA-handled prospect call.
- **End user:** Prospects calling the ARIA intake line. They never touch this service directly — they just have a 10–15 minute conversation with the ARIA voice agent.

## What ARIA does for InSync Tech

ARIA is a voice agent (ElevenLabs-driven) that handles inbound intake calls for InSync Tech. Instead of Ian manually filling out the ARIA Client Intake Form by phone, ARIA conducts the interview, gathers all the data points the form needs, and hands them off to this pipeline to render into the filing artifacts (PDF summary + populated .docx form) and email.

The business value: **Ian gets a populated, filing-ready intake packet in his inbox 90 seconds after the call ends. No data entry.**

## Vocabulary that means something specific

| Term | Meaning |
|---|---|
| **Intake** | The first-call data-collection step in InSync Tech's onboarding |
| **ARIA** | The voice agent persona (ElevenLabs); the brand-facing AI |
| **Filing copy** | The populated `.docx` form that goes into the client folder |
| **Summary** | The ReportLab PDF that gives Ian a one-page recap of what ARIA gathered |
| **Welcome packet** | A downstream artifact, sent to the client after intake (see ARIA_Welcome_Packet.docx) |
| **Service agreement** | A downstream contract artifact (see ARIA_Service_Agreement_Template.docx) |

## Workflows the substrate must respect

1. Prospect calls intake number → ARIA conducts interview → call ends.
2. ElevenLabs fires post-call webhook here → we verify HMAC → extract → render → email Ian.
3. Ian reviews in inbox → saves `.docx` to client folder → optionally triggers follow-up.
4. Follow-up: SMS or email (managed by `follow_up_engine.py` + `sms_sender.py` / `followup_email.py`).

## Things that look generic but aren't

- The intake form fields are **InSync Tech-specific**. Don't auto-replace them with generic CRM fields when refactoring `extractor.py`.
- The `.docx` template at root (ARIA_Client_Intake_Form_v4.docx) is the **source-of-truth form layout**. The populated artifact must mirror that layout exactly — clients see it on file.
