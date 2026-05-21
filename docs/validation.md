# Validation — insynctech-pipeline

> **What this file is:** input/output validation rules. VERIFICATION (BIRDS-01).

## Inbound validation
1. **HMAC signature** — first gate; reject 401 if missing or invalid
2. **Webhook body shape** — FastAPI request parsing; missing required fields → 400
3. **Transcript presence** — if the call ended with no transcript (silent call, etc.), skip extraction; return 200 with `{"status": "skipped_empty_transcript"}`

## Extraction validation
- `extractor.py` should return a JSON object with the canonical ARIA intake form fields. If extraction returns nothing or invalid JSON, fall back to a minimal record (business name + transcript URL) so the email still goes out — operator can manually fill the rest.

## Output validation
- PDF generation must not crash on missing fields; render empty placeholders for absent values
- DOCX form population must not crash on missing fields; leave checkboxes unchecked / write-ins blank

## What this file is NOT
- A duplicate of the extractor prompt. The prompt IS the schema definition; this is the validation behavior around it.
