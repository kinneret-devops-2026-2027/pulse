# 💓 Pulse — the class status page

> DevOps & Cloud Infrastructure · Kinneret College · 2026–2027
> One service. Six teams. One `main` branch. A real release every few weeks.

Pulse checks whether services are alive and shows it on one screen — the same
kind of tool every DevOps team keeps open on the big monitor.
We build it together through the whole semester: Git → CI → Docker → Cloud → Monitoring.

## Run it locally (3 commands)

```bash
# macOS / Linux
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

```bash
# Windows (Git Bash in VS Code)
py -m venv .venv && source .venv/Scripts/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open <http://127.0.0.1:8000> · API docs: <http://127.0.0.1:8000/docs>

Run the tests: `pytest -q`

## Endpoints

| Endpoint | Owner | What it returns |
|---|---|---|
| `GET /health` | everyone | `{"status":"ok"}` — is the process alive? |
| `GET /version` | Team 6 | version + commit SHA + environment |
| `GET /api/services` | Team 1 | list of monitored services |
| `GET /api/status` | Team 2 | live check of every service |
| `GET /api/teams` | everyone | who built this |

## The six teams

| # | Team | Owns | Semester path |
|---|---|---|---|
| 1 | 🛰️ Mission Control | `app/main.py`, `app/storage.py` | API → database → config |
| 2 | 🩺 Heartbeat | `app/checker.py` | checks → scheduler → metrics |
| 3 | 🖥️ Big Screen | `app/static/` | status page → history → dashboards |
| 4 | 🚨 Siren | `app/alerts.py` | alert text → webhooks + secrets |
| 5 | 🧪 Gatekeepers | `tests/`, `.github/` | tests → CI pipeline → quality gates |
| 6 | 🚀 Launch Crew | `app/version.py`, `CHANGELOG.md` | releases → Docker image → deploy |

See [CONTRIBUTING.md](CONTRIBUTING.md) for the workflow and `docs/missions/` for each team's first mission.
