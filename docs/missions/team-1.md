# 🛰️ Team 1 — Mission Control · first mission

**Goal:** Ops want to ask about ONE service: `GET /api/services/github`.

**Branch:** `team-1/get-service-by-id`
**Files:** `app/main.py`, `tests/test_api.py`, `teams/team-1.json`

## Steps
1. Add the endpoint in `app/main.py` (under the Team 1 comment):
   ```python
   @app.get("/api/services/{service_id}")
   def get_service(service_id: str):
       service = storage.find_service(service_id)
       if service is None:
           raise HTTPException(status_code=404, detail="service not found")
       return service
   ```
2. Delete the `pytestmark = ...` line in `tests/test_api.py`.
3. `pytest -q` → green. Try it: <http://127.0.0.1:8000/api/services/github>
4. Commit: `feat: add GET /api/services/{id} with 404 for missing id`

**Done when:** tests pass, PR approved by another team, merged.
