"""Where the list of monitored services lives.

For now: a JSON file (data/services.json).
Later in the semester Team 1 may replace this with a real database.
"""

import json
from pathlib import Path

from .config import BASE_DIR

DATA_FILE: Path = BASE_DIR / "data" / "services.json"


def load_services() -> list[dict]:
    with DATA_FILE.open(encoding="utf-8") as f:
        return json.load(f)


def find_service(service_id: str) -> dict | None:
    for service in load_services():
        if service["id"] == service_id:
            return service
    return None
