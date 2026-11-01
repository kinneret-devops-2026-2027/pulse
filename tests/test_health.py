from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_is_ok():
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}


def test_services_list_not_empty():
    r = client.get("/api/services")
    assert r.status_code == 200
    assert len(r.json()) >= 1
