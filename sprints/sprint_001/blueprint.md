# Sprint 001 — blueprint

> Order of operations.

## Order
1. **Cabinet merge** — review scaffold; fast-forward `cabinet-refactor` → `main`.
2. **Persistence walk** — read `follow_up_engine.py` end-to-end; document where follow-up state lives. If volatile, add to `planning/risks.md`.
3. **Alive test** — POST a synthetic webhook payload with valid HMAC against the prod URL; confirm email lands.

## Why this order
- Cabinet first so subsequent work has a place to land.
- Persistence walk is read-only; can happen in parallel.
- Alive test is the cheapest end-to-end signal we have.
