# AGENTS.md — router

**The first file every agent reads.** Tell the substrate where to look before it guesses.

## Project: insynctech-pipeline (ARIA Intake Pipeline)

FastAPI service that receives ElevenLabs post-call webhooks from the ARIA intake agent, extracts structured client data with Claude Haiku, generates a populated intake PDF + DOCX, and emails them via Resend. Deploys to Railway.

## How to navigate this Cabinet

1. **`planning/domain.md`** — the InSync Tech business context: who the intake agent is for, what the form means.
2. **`planning/decisions.md`** — append-only house rules.
3. **`sprints/sprint_001/requirements.md`** — what "done" means this sprint.
4. **`docs/architecture.md`** — the pipeline (webhook → extract → render → email).
5. **`docs/api.md`** — webhook contract + HMAC verification.

## Code location

This repo is **flat** — Python source files sit at the root (`main.py`, `extractor.py`, etc.), not in `src/`. The Procfile says `uvicorn main:app`. Cabinet doctrine says code lives in `src/` — there is an open question + decision in `planning/` about whether to restructure. Until then, treat **the repo root** as the canonical source dir, ignoring the `docs/`, `planning/`, `sprints/` Cabinet trees.

## Document templates

`.docx` and `.pdf` files at root (ARIA_Client_Intake_Form_v4.docx, ARIA_Welcome_Packet.docx, etc.) are **design-time references**, not loaded at runtime. They should eventually move to `templates/` — see `planning/decisions.md`.

## When you're stuck

- New ambiguity? → write the question to `planning/questions.md` and pause.
- New gotcha? → append to `planning/risks.md`.
- New rule the team agreed on? → append to `planning/decisions.md` (NEVER edit older entries).

## When you finish work

- Update `sprints/sprint_001/handoff.md`.
- Update `planning/state.md`.

## BIRDS cycle — your loop
Verification (`docs/` + `domain.md`) → Decision (`decisions.md`) → Correction (`risks.md`) → Documentation (`handoff.md`) → Learning (`state.md`).
