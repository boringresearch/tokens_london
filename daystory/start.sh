#!/usr/bin/env bash
set -euo pipefail
cd "$(dirname "$0")"
set -a
source /config/team-25.config
set +a
export COSMOS3_REASON_URL="${COSMOS3_REASON_URL:-http://166.19.38.112:8001}"
exec .venv/bin/gunicorn --bind 127.0.0.1:7860 --workers 1 --threads 4 --timeout 300 app:app
