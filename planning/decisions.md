# Decisions — insynctech-pipeline

> **BIRDS-02 (DECISION)** — the **append-only** gradient. NEVER edit or delete past entries. New decisions go at the bottom.

---

## 2026-05-21 · Adopt Cabinet scaffold
- **Decision:** This repo follows the 18-file DVE Cabinet structure (Tier 1 pillar).
- **Reason:** Aligns the substrate (Claude Code / Aria Code) with the project's BIRDS cycle.

---

## 2026-05-21 · Cabinet refactor on `cabinet-refactor` branch first
- **Decision:** Cabinet scaffold gets added on a branch, NOT main.
- **Reason:** Reversibility while pattern is being validated across repos.

---

## 2026-05-21 · Keep flat code layout for now
- **Decision:** Python source files stay at the repo root (`main.py`, `extractor.py`, etc.). Procfile (`uvicorn main:app`) and every flat import remain unchanged.
- **Reason:** This is a single-purpose webhook service; flat layout is idiomatic and a `src/` reshape would touch every file for no functional gain. Cabinet doctrine on `src/` exists for cognitive clarity; this repo is small enough that the README + Cabinet docs provide the same clarity without the rename.
- **Tracked as:** question logged in `planning/questions.md` for later revisit (when project scales or when DCU audit forces consistency).

---

## 2026-05-21 · `.docx` / `.pdf` templates remain at root for now
- **Decision:** The ARIA_*.docx and ARIA_*.pdf design-reference files stay at repo root. They are not loaded at runtime, so moving them is purely cosmetic.
- **Reason:** Risk-free move yields no behavioral change; defer to the future "templates/" reorg if/when more templates accrue.
- **Tracked as:** open question in `planning/questions.md`.

---

<!-- Append new decisions BELOW this comment. Never edit above. -->
