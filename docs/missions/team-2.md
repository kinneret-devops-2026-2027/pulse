# 🩺 Team 2 — Heartbeat · first mission

**Goal:** right now every service shows `unknown`. Teach Pulse to say `up` / `slow` / `down`.

**Branch:** `team-2/classify-status`
**Files:** `app/checker.py`, `tests/test_checker.py`, `teams/team-2.json`

## Steps
1. Implement `classify()` in `app/checker.py` using the rules in its docstring
   (`SLOW_THRESHOLD_MS` is already imported).
2. Delete the `pytestmark = ...` line in `tests/test_checker.py`.
3. `pytest -q` → 6 new green tests.
4. Run the app — the Status column now shows real words.
5. Commit: `feat: classify service status as up/slow/down`

**Done when:** tests pass, PR approved by another team, merged.
