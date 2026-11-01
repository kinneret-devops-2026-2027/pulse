# 🚀 Team 6 — Launch Crew · first mission

**Goal:** ship **Pulse v0.1.0** at the end of the class.

**Branch:** `team-6/release-v0.1.0`
**Files:** `app/version.py`, `CHANGELOG.md`, `teams/team-6.json`

## Steps
1. While others work: follow their PRs on GitHub and draft the CHANGELOG entries.
2. When missions 1–5 are merged:
   ```bash
   git switch main && git pull
   git switch -c team-6/release-v0.1.0
   ```
3. `app/version.py`: `"0.1.0-dev"` → `"0.1.0"`.
4. `CHANGELOG.md`: rename `[Unreleased]` to `[0.1.0] - <today>`, list every merged mission.
5. Commit: `chore: release v0.1.0` → PR → review → merge.
6. Tag and publish:
   ```bash
   git switch main && git pull
   git tag -a v0.1.0 -m "Pulse v0.1.0 - first class release"
   git push origin v0.1.0
   ```
7. GitHub → Releases → *Draft a new release* → choose `v0.1.0` → paste the CHANGELOG notes → Publish.
8. Open `/version` on the lecturer's screen: `0.1.0` + the commit SHA. 🎉

**Done when:** tag `v0.1.0` exists on GitHub and a Release is published.
