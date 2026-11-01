"""Team 4 - Siren. Remove the pytestmark line when format_alert() is implemented."""

import pytest

from app.alerts import format_alert

pytestmark = pytest.mark.skip(reason="Mission Team 4 - delete this line when format_alert() is ready")


def test_no_alert_when_nothing_changed():
    assert format_alert("GitHub", "up", "up") is None


def test_alert_when_service_goes_down():
    assert format_alert("GitHub", "up", "down") == "🔴 GitHub: up → down"


def test_alert_when_service_recovers():
    assert format_alert("PyPI", "down", "up") == "🟢 PyPI: down → up"
