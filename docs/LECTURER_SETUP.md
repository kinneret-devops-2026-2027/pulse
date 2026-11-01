# Lecturer setup — before the class (≈20 minutes)

## 1. Organization + repo
1. GitHub → **+** → *New organization* → Free plan → name e.g. `kinneret-devops-2027`.
2. Create the repo **`pulse`** — **Public** (branch protection is free on public repos in a Free org;
   for a private repo you need GitHub Team — teachers can request it through GitHub Education).
   Leave it empty (no README / .gitignore / license).
3. Push this starter:
   ```bash
   cd pulse
   git init -b main
   git add .
   git commit -m "chore: starter project for Pulse"
   git remote add origin git@github.com:<ORG>/pulse.git
   git push -u origin main
   ```

## 2. People and teams
1. Org → **People** → *Invite member* → paste the students' GitHub usernames.
2. Org → **Teams** → create `staff`, `team-1` … `team-6`, add students.
3. Repo → Settings → **Collaborators and teams** → give every team-N the **Write** role.
4. (Optional) Un-comment `.github/CODEOWNERS` and replace `ORG`.

## 3. Protect `main`
Repo → Settings → **Branches** → *Add branch ruleset* (or classic *branch protection rule*) for `main`:
- ✅ Require a pull request before merging — **1 approval**
- ✅ Dismiss stale approvals when new commits are pushed
- ✅ Block force pushes · ✅ Restrict deletions
- (next lecture, after CI exists) ✅ Require status checks to pass
- Repo → Settings → General → Pull Requests: allow **Squash merging** only, ✅ *Automatically delete head branches*

## 4. Issues
With the GitHub CLI logged in (`gh auth login`):
```bash
bash scripts/create_issues.sh <ORG>/pulse
```
Creates one `mission` issue per team from `docs/missions/team-N.md`.

## 5. In class — the release party
- Project the repo's **Pull requests** tab and the **Insights → Network** graph.
- When Team 6 pushes `v0.1.0`, run the app from a fresh clone of `main` and open `/version`.
