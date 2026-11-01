"""Team 1 - Mission Control. Remove the pytestmark line when your endpoint is ready."""

import pytest
from fastapi.testclient import TestClient

from app.main import app

pytestmark = pytest.mark.skip(reason="Mission Team 1 - delete this line when GET /api/services/{id} exists")

client = TestClient(app)


def test_get_existing_service():
    r = client.get("/api/services/github")
    assert r.status_code == 200
    assert r.json()["name"] == "GitHub API"


def test_missing_service_is_404():
    r = client.get("/api/services/does-not-exist")
    assert r.status_code == 404
