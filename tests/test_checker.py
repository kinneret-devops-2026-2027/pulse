"""Team 2 - Heartbeat. Remove the pytestmark line when classify() is implemented."""

import pytest

from app.checker import classify

pytestmark = pytest.mark.skip(reason="Mission Team 2 - delete this line when classify() is ready")


@pytest.mark.parametrize(
    "status_code, latency_ms, expected",
    [
        (200, 120, "up"),
        (301, 50, "up"),
        (200, 2500, "slow"),
        (503, 40, "down"),
        (404, 40, "down"),
        (None, None, "down"),
    ],
)
def test_classify(status_code, latency_ms, expected):
    assert classify(status_code, latency_ms) == expected
