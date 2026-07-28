# Auto-updating “Last updated” date (GitHub Actions)

This repository automatically updates the `README.md` with the current UTC date in `YYYY-MM-DD` format.

## What it does
- Every day, a GitHub Actions workflow runs.
- It replaces the placeholder `{{LAST_UPDATED}}` in `README.md` with today’s UTC date (YYYY-MM-DD).
- If the date changes, the workflow commits the updated `README.md` back to the repository.

## Setup

### 1) Add the placeholder to `README.md`
In `README.md`, include this line where you want the date to appear:

`Last updated: {{LAST_UPDATED}}`

### 2) Add the workflow file
Create the workflow at:

`.github/workflows/update-readme-date.yml`

Example workflow:

```yml
name: Update README date (UTC)

on:
  schedule:
    - cron: "0 0 \* \* \*"   # daily at 00:00 UTC
  workflow\_dispatch: {}

jobs:
  update:
    runs-on: ubuntu-latest
    permissions:
      contents: write

    steps:
      - uses: actions/checkout@v4

      - name: Update README with UTC date (YYYY-MM-DD)
        run: |
          DATE="\$(date -u +"%Y-%m-%d")"
          sed -i "s/{{LAST\_UPDATED}}/\$DATE/" README.md

      - name: Commit if changed
        run: |
          if git diff --quiet; then
            echo "No changes."
            exit 0
          fi
          git config user.name "github-actions[bot]"
          git config user.email "github-actions[bot]@users.noreply.github.com"
          git add README.md
          git commit -m "Update README last updated date to \$(date -u +"%Y-%m-%d")"
          git push
