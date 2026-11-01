# 🧪 Team 5 — Gatekeepers · first mission

**Goal:** protect the contract Ops depend on, and guard `main` by reviewing.

**Branch:** `team-5/version-contract-test`
**Files:** `tests/test_contract.py` (new), `teams/team-5.json`

## Steps
1. Create `tests/test_contract.py`:
   ```python
   import re
   from fastapi.testclient import TestClient
   from app.main import app

   SEMVER = re.compile(r"^\d+\.\d+\.\d+(-[0-9A-Za-z.]+)?$")
   client = TestClient(app)

   def test_version_contract():
       body = client.get("/version").json()
       assert SEMVER.match(body["version"]), body["version"]
       assert body["commit"]
       assert "env" in body
   ```
2. `pytest -q` → green.
3. Commit: `test: add /version contract test`
4. **Review duty:** you are the default reviewers tonight. For each PR check:
   tests green? template filled? no secrets? small and clear? Comment, then approve.

**Done when:** your PR is merged and you reviewed at least 2 PRs of other teams.
