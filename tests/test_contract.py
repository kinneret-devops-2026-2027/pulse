
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
