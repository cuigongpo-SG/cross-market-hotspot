#!/usr/bin/env bash
set -euo pipefail

# Simple placeholder for Codex CLI review.
# In a real setup you would call:
#   codex exec --task review --repo-path . --model openai/gpt-oss-120b:free --prompt "..."
# Here we just echo a dummy message to keep CI passing.

echo "Running Codex CLI review (placeholder)…"
# Simulate a successful review
cat <<'MSG'
=== Codex Review Summary ===
- No issues found (placeholder).
MSG

exit 0
