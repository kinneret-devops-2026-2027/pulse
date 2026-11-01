"""Pulse - a tiny status page built by the whole class.

Run locally:
    uvicorn app.main:app --reload
Then open http://127.0.0.1:8000
"""

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles

from . import storage
from .checker import check_all
from .config import APP_ENV, BASE_DIR, git_commit
from .teams import load_teams
from .version import __version__

app = FastAPI(title="Pulse", version=__version__)
STATIC_DIR = BASE_DIR / "app" / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", include_in_schema=False)
def index():
    return FileResponse(STATIC_DIR / "index.html")


# ---------- Ops endpoints: who am I and am I alive? ----------
@app.get("/health")
def health():
    return {"status": "ok"}


@app.get("/version")
def version():
    return {"version": __version__, "commit": git_commit(), "env": APP_ENV}


# ---------- Team 1 - Mission Control (API) ----------
@app.get("/api/services")
def list_services():
    return storage.load_services()


# MISSION (Team 1): add  GET /api/services/{service_id}
#   * return the service dict when it exists
#   * raise HTTPException(status_code=404) when it does not
#   * then remove the skip marker in tests/test_api.py


# ---------- Team 2 - Heartbeat (checker) ----------
@app.get("/api/status")
async def status():
    return await check_all(storage.load_services())


# ---------- Everyone - who built this? ----------
@app.get("/api/teams")
def teams():
    return load_teams()


__all__ = ["app", "HTTPException"]
