#!/usr/bin/env bash
# Create one GitHub issue per team mission.
# usage: bash scripts/create_issues.sh <ORG>/pulse      (requires: gh auth login)
set -euo pipefail
REPO="${1:?usage: create_issues.sh <ORG>/pulse}"
NAMES=("" "Mission Control" "Heartbeat" "Big Screen" "Siren" "Gatekeepers" "Launch Crew")

gh label create mission --repo "$REPO" --color 8b93f8 --description "Team mission" 2>/dev/null || true
for n in 1 2 3 4 5 6; do
  gh label create "team-$n" --repo "$REPO" --color 43c6e8 2>/dev/null || true
  gh issue create --repo "$REPO" \
    --title "[team-$n] ${NAMES[$n]} - first mission" \
    --body-file "docs/missions/team-$n.md" \
    --label mission --label "team-$n"
done
echo "✓ 6 mission issues created in $REPO"
