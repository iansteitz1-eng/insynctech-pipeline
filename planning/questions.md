# Open questions — insynctech-pipeline

> Where the substrate parks ambiguity.

---

## 2026-05-21 · Move templates to `templates/` directory?
- **Q:** Move ARIA_*.docx/.pdf files into a `templates/` directory? They're not loaded at runtime, so this is cosmetic only.
- **Blocks:** Cabinet doctrine "asset location" cleanliness; nothing functional.
- **Who:** Ian.

## 2026-05-21 · Restructure code into `src/` at some point?
- **Q:** Cabinet doctrine says code lives in `src/`. We chose flat for now (see decisions.md). Worth revisiting once the project grows past ~15 files or when a second service joins this repo?
- **Blocks:** Cross-repo doctrine consistency; nothing functional.
- **Who:** Ian (or future-Ian during DCU audit).

## 2026-05-21 · Follow-up engine persistence
- **Q:** Does `follow_up_engine.py` persist follow-up state across restarts? If yes, where? If not, are we losing follow-ups when Railway redeploys?
- **Blocks:** Reliability story.
- **Who:** Code-walk to verify.

---

<!-- Append below. Move resolved questions to decisions.md. -->
