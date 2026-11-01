"""Reads teams/*.json - every team adds its own file, so nobody edits the same file."""

import json

from .config import BASE_DIR

TEAMS_DIR = BASE_DIR / "teams"


def load_teams() -> list[dict]:
    teams = []
    for path in sorted(TEAMS_DIR.glob("team-*.json")):
        try:
            teams.append(json.loads(path.read_text(encoding="utf-8")))
        except json.JSONDecodeError:
            teams.append({"team": path.stem, "name": "⚠️ invalid JSON", "members": []})
    return teams
