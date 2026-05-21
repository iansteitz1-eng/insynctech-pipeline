# Sprint 001 — acceptance criteria

## 1. Cabinet scaffold merged
- `git log main --oneline` shows the Cabinet commit
- All 18 Cabinet files present

## 2. Persistence question answered
- `planning/questions.md` no longer carries the follow-up-engine-persistence question
- `planning/decisions.md` has an entry: "follow-up state persists via X" OR "follow-up state is volatile — risk accepted / mitigation Y"

## 3. Alive test passed
- Email arrives in `ian@insynctech.io` within ~90 seconds of test webhook
- Both attachments present (PDF + DOCX)
- `planning/state.md` Recent section logs the alive-test result with timestamp
