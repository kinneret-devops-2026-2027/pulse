"""Configuration comes from environment variables - never from code.

Copy .env.example to .env and edit it locally.
.env is listed in .gitignore: secrets never enter Git.
"""

import os
import subprocess
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def _load_dotenv(path: Path) -> None:
    """Tiny .env loader (KEY=VALUE lines) so we need no extra dependency."""
    if not path.exists():
        return
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#") or "=" not in line:
            continue
        key, value = line.split("=", 1)
        os.environ.setdefault(key.strip(), value.strip())


_load_dotenv(BASE_DIR / ".env")

APP_ENV = os.getenv("APP_ENV", "local")
CHECK_TIMEOUT_SECONDS = float(os.getenv("CHECK_TIMEOUT_SECONDS", "3"))
SLOW_THRESHOLD_MS = int(os.getenv("SLOW_THRESHOLD_MS", "800"))
# Secret! Lives only in .env locally and in GitHub Secrets later in the semester.
ALERT_WEBHOOK_URL = os.getenv("ALERT_WEBHOOK_URL", "")


def git_commit() -> str:
    """Short commit SHA of the running code - lets Ops know exactly what is deployed."""
    env_sha = os.getenv("GIT_COMMIT")
    if env_sha:
        return env_sha[:7]
    try:
        out = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=BASE_DIR, capture_output=True, text=True, timeout=2,
        )
        return out.stdout.strip() or "unknown"
    except Exception:
        return "unknown"
