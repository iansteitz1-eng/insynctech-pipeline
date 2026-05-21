# Sprint 001 — handoff

> **BIRDS-04 (DOCUMENTATION)** — what shipped this sprint, why, where to find it.

## In-flight (as of 2026-05-21)

### 1. Cabinet scaffold — IN REVIEW
- Where: `cabinet-refactor` branch
- Files: 17 new (AGENTS.md, CLAUDE.md, docs/*, planning/*, sprints/sprint_001/*)
- Status: scaffold written; awaiting review + merge to `main`
- Notes: kept flat code layout; kept templates at root — both deferred per decisions.md

### 2. Persistence walk — NOT STARTED
- Target: `follow_up_engine.py`

### 3. Alive test — NOT STARTED
- Synthetic HMAC-signed webhook payload against prod URL

## Risks accepted this sprint
- See `planning/risks.md` (HMAC silent-fatal, extractor fallback, public repo exposure)

## Next sprint candidates
- Template reorg into `templates/`
- Code reshape into `src/` (only if/when project grows past ~15 files)
- Cron-based weekly alive test
