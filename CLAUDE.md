# CLAUDE.md — thin adapter

This file is the builder-facing entrypoint. The substrate (Claude Code or Aria Code) reads it on session start.

**Defer all substantive context to `AGENTS.md` and the Cabinet.** This file is just the handoff.

## Read order for this project
1. `AGENTS.md` (router)
2. `planning/domain.md`, `planning/decisions.md`
3. `sprints/sprint_001/requirements.md`
4. `docs/` as needed

## Tooling notes
- Stack: Python 3, FastAPI, Anthropic SDK (Claude Haiku), ReportLab, python-docx, Resend
- Code dir: repo root (flat). NOT `src/` — see decisions.md.
- Run dev: `uvicorn main:app --reload`
- Deploy: Railway via `Procfile` (`web: uvicorn main:app --host 0.0.0.0 --port $PORT`) + `nixpacks.toml`
- HMAC: ElevenLabs webhook secret in env; verified in `main.py` before processing

## Substrate hooks
None enabled yet for this project. Hooks live substrate-wide in `~/.claude/settings.json`.
