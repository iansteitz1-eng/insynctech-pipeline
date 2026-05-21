# Risks — insynctech-pipeline

> **BIRDS-03 (CORRECTION)** — gotchas, near-misses, prior failures. Append-only.

---

## 2026-05-21 · HMAC secret rotation is silent-fatal
- **Risk:** If the ElevenLabs webhook secret is rotated without updating `ELEVENLABS_WEBHOOK_SECRET` env on Railway, every inbound call will fail HMAC and silently drop. Ian gets no email and no error notification.
- **Mitigation:** When rotating, update Railway env BEFORE rotating in ElevenLabs. Consider a low-cost cron that fires a test call weekly to verify the pipeline is alive end-to-end.

---

## 2026-05-21 · Extractor failure mode
- **Risk:** Claude Haiku occasionally returns malformed or empty JSON. Without a fallback, the pipeline crashes silently in the background task.
- **Mitigation:** `validation.md` calls for a minimal-record fallback. Verify this is implemented; if not, add it.

---

## 2026-05-21 · Repo is PUBLIC on GitHub
- **Risk:** Per `reference_github_inventory_2026_05_20.md`, this repo is PUBLIC. Any secret accidentally committed is immediately exposed. Code, prompts, and form templates are all viewable.
- **Mitigation:** Never commit `.env`. Treat the README and Cabinet docs as customer-facing surface. Be careful with InSync-specific business logic that might be commercially sensitive.

---

<!-- Append new risks below this line. -->
