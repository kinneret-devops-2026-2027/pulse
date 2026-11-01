# 🚨 Team 4 — Siren · first mission

**Goal:** prepare the exact alert text. Later in the semester it will be sent to a chat
through a webhook whose URL is a **secret** (`ALERT_WEBHOOK_URL` in `.env`, never in Git).

**Branch:** `team-4/alert-message`
**Files:** `app/alerts.py`, `tests/test_alerts.py`, `teams/team-4.json`

## Steps
1. Implement `format_alert()` using the rules in its docstring (`EMOJI` dict is ready).
2. Delete the `pytestmark = ...` line in `tests/test_alerts.py`.
3. `pytest -q` → 3 new green tests.
4. Commit: `feat: format status-change alert messages`
5. Bonus: copy `.env.example` to `.env`, put a fake URL in it and run `git status` —
   prove that `.env` is ignored.

**Done when:** tests pass, PR approved by another team, merged.
