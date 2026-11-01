"""Siren - tells humans when something changes.   (Team 4 owns this file)"""

EMOJI = {"up": "🟢", "slow": "🟡", "down": "🔴", "unknown": "⚪"}


def format_alert(service_name: str, old_status: str, new_status: str) -> str | None:
    """Build the alert text sent to the team chat.

    MISSION (Team 4 - Siren): implement and remove the skip marker in
    tests/test_alerts.py.

      * if old_status == new_status       -> return None (no alert, no noise!)
      * otherwise return exactly:
        "<emoji of new> <service_name>: <old_status> → <new_status>"
        example: "🔴 GitHub: up → down"
    """
    return None  # TODO(team-4): replace with the real rules
