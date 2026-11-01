# How we work — the Pulse workflow

`main` is protected. Nobody pushes to it directly — not even the lecturer.
Every change travels the same road:

```
Issue → Branch → Commits → Push → Pull Request → Review (+ checks) → Merge → Release
```

## 1. Start from an issue
Every change has an issue. Assign it to yourself.

## 2. Branch naming
```
team-<N>/<short-description>
```
Examples: `team-2/classify-status`, `team-3/status-badges`

```bash
git switch main
git pull
git switch -c team-2/classify-status
```

## 3. Commit messages — Conventional Commits
```
<type>: <what changed, in the imperative>
```
| type | when |
|---|---|
| `feat` | new behaviour for users |
| `fix` | bug fix |
| `test` | tests only |
| `docs` | documentation only |
| `chore` | maintenance (deps, config) |
| `ci` | pipeline changes |

Good: `feat: add GET /api/services/{id} with 404 for missing id`
Bad: `update`, `fix stuff`, `final final 2`

Reference the issue in the PR description: `Closes #3`.

## 4. Before you push
```bash
pytest -q          # all green (skipped is OK for other teams' missions)
git status         # nothing unexpected, no .env, no .venv
```

## 5. Pull Request rules
* Fill the PR template (what / why / how tested / Ops impact).
* **At least one approval from a member of a different team.**
* Small PRs win. If a PR touches files of another team — tag that team.
* Merge method: **Squash and merge** → one clean commit per change on `main`.
* Delete the branch after merge.

## 6. Never commit
* `.env`, tokens, passwords, private keys (`id_ed25519` without `.pub`!)
* `.venv/`, `__pycache__/`
* Big binary files

Leaked a secret? **Tell the lecturer immediately and revoke/rotate the secret.**
Deleting it in a new commit is not enough — it is still in the history.

## 7. Releases (Team 6)
* Bump `app/version.py` and `CHANGELOG.md` in one PR: `chore: release v0.1.0`
* After it is merged, tag `main`:
```bash
git switch main && git pull
git tag -a v0.1.0 -m "Pulse v0.1.0 - first class release"
git push origin v0.1.0
```
* Create a GitHub Release from the tag with the CHANGELOG notes.
