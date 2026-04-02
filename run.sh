#!/bin/bash
# GhostTrack - run script
# Usage: bash run.sh

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Install dependencies if not present
if ! python3 -c "import requests, phonenumbers" 2>/dev/null; then
    echo "[*] Installing dependencies..."
    pip3 install -r "$SCRIPT_DIR/requirements.txt"
fi

python3 "$SCRIPT_DIR/GhostTR.py"
