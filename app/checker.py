"""Heartbeat - checks whether a service is alive.   (Team 2 owns this file)"""

import asyncio
import time

import httpx

from .config import CHECK_TIMEOUT_SECONDS, SLOW_THRESHOLD_MS

UP, SLOW, DOWN, UNKNOWN = "up", "slow", "down", "unknown"


def classify(status_code: int | None, latency_ms: float | None) -> str:
    """Turn one HTTP result into a status word.

    MISSION (Team 2 - Heartbeat): implement the rules below and remove the
    skip marker in tests/test_checker.py so the tests run.

      * no response at all (status_code is None)      -> "down"
      * status code 500 or higher                     -> "down"
      * status code 2xx/3xx but latency >= SLOW_THRESHOLD_MS -> "slow"
      * status code 2xx/3xx and fast                  -> "up"
      * anything else (e.g. 404)                      -> "down"
    """
    return UNKNOWN  # TODO(team-2): replace with the real rules


async def check_one(client: httpx.AsyncClient, service: dict) -> dict:
    start = time.perf_counter()
    status_code = None
    try:
        response = await client.get(service["url"], timeout=CHECK_TIMEOUT_SECONDS)
        status_code = response.status_code
    except httpx.HTTPError:
        pass
    latency_ms = round((time.perf_counter() - start) * 1000, 1)
    return {
        "id": service["id"],
        "name": service["name"],
        "url": service["url"],
        "status": classify(status_code, latency_ms if status_code else None),
        "http_status": status_code,
        "latency_ms": latency_ms if status_code else None,
        "checked_at": time.strftime("%Y-%m-%dT%H:%M:%S"),
    }


async def check_all(services: list[dict]) -> list[dict]:
    headers = {"User-Agent": "Pulse-status-checker/1.0 (Kinneret DevOps course)"}
    async with httpx.AsyncClient(follow_redirects=True, headers=headers) as client:
        return await asyncio.gather(*(check_one(client, s) for s in services))
