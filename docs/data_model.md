# Data model — insynctech-pipeline

> **What this file is:** the shapes the pipeline produces and consumes. VERIFICATION (BIRDS-01).

This service has no persistent database. Data shapes are transient (per-webhook). The "model" is the extraction schema.

## Inbound: ElevenLabs post-call webhook
- Headers: HMAC signature + timestamp
- Body: ElevenLabs call payload (transcript, agent metadata, call metadata)
- Verified in `main.py` before processing

## Internal: extracted JSON
- Produced by `extractor.py` via Claude Haiku
- Shape: ARIA intake form fields (business name, contact info, services interested in, budget tier, scheduling notes, etc.)
- The canonical field set lives in `extractor.py`'s prompt — that prompt is the de-facto schema definition

## Outbound: PDF + DOCX artifacts
- `ARIA_Intake_Summary_<business>_<date>.pdf` — extracted-data report (ReportLab)
- `ARIA_Intake_Form_<business>_<date>.docx` — populated intake form (python-docx)

## Outbound: email
- To: `ian@insynctech.io` (the InSync Tech inbox)
- Subject: business name + date
- Attachments: the two artifacts above
- Body: inline summary

## What is NOT modelled here
- No DB rows. No user/agent persistence. Each webhook is self-contained.
- Follow-up state, if persisted, lives in `follow_up_engine.py`'s store (verify if/how it persists across restarts).
