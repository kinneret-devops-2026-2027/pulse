# Team missions — first class (Git workflow)

Every team, every mission, the same 4 moves:

1. **Team file** — the driver creates the branch and `teams/team-N.json`:
   ```json
   {"team": "team-N", "name": "Team name", "emoji": "🛰️", "members": ["Driver Name"]}
   ```
   Commit `docs: add team-N members file`, push.
2. **Everyone signs** — each member fetches the branch, adds their own name to `members`,
   commits and pushes. Rejected push? `git pull` first, resolve the conflict if any, push again.
3. **The code mission** — see `team-N.md`.
4. **PR** → review by another team → squash & merge → delete branch.

| Team | Mission file |
|---|---|
| 1 🛰️ Mission Control | [team-1.md](team-1.md) |
| 2 🩺 Heartbeat | [team-2.md](team-2.md) |
| 3 🖥️ Big Screen | [team-3.md](team-3.md) |
| 4 🚨 Siren | [team-4.md](team-4.md) |
| 5 🧪 Gatekeepers | [team-5.md](team-5.md) |
| 6 🚀 Launch Crew | [team-6.md](team-6.md) |
