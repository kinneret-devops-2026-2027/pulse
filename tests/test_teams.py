"""Every teams/team-N.json must be valid - this protects the status page footer."""

import json

import pytest

from app.teams import TEAMS_DIR

TEAM_FILES = sorted(TEAMS_DIR.glob("team-*.json"))


@pytest.mark.parametrize("path", TEAM_FILES, ids=lambda p: p.name)
def test_team_file_is_valid(path):
    data = json.loads(path.read_text(encoding="utf-8"))
    assert isinstance(data.get("name"), str) and data["name"].strip()
    assert isinstance(data.get("members"), list) and len(data["members"]) >= 1
    assert data.get("team") == path.stem, "field 'team' must match the file name"
