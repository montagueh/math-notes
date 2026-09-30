#!/bin/bash
TARGET_DIR="/Users/monte/Documents/maths/" # Path to local github

cd "$TARGET_DIR" || exit

# Stage the files
git add -A

# Commit with timestamped message; check if there are changes to avoid empty commits
if ! git diff-index --quiet HEAD --; then
  git commit -m "Automated backup: $(date '+%Y-%m-%d %H:%M:%S')"
  git push origin main
fi
