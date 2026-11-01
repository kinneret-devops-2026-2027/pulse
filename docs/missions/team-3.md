# 🖥️ Team 3 — Big Screen · first mission

**Goal:** the status page must be readable from the back of the room.

**Branch:** `team-3/status-badges`
**Files:** `app/static/app.js`, `app/static/style.css`, `teams/team-3.json`

## Steps
1. In `statusCell()` return a coloured badge:
   `'<span class="badge badge-' + status + '">' + status + '</span>'` (CSS is ready).
2. In `renderSummary()` write into `#summary` the text `X / Y services up`.
3. Reload the browser (Ctrl+Shift+R / Cmd+Shift+R) and check.
4. Commit: `feat: coloured status badges and up-count summary`

**Tip:** until Team 2 merges, statuses are `unknown` → grey badges. That is fine:
your code is correct when Team 2's code arrives. This is integration.

**Done when:** works in the browser, PR approved by another team, merged.
