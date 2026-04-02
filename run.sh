#!/bin/bash
# GhostTrack - run script
SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"

# Aktifkan venv jika ada
if [ -f "$SCRIPT_DIR/venv/bin/activate" ]; then
    source "$SCRIPT_DIR/venv/bin/activate"
fi

# Install dependencies jika belum ada
if ! python3 -c "import requests, phonenumbers" 2>/dev/null; then
    echo "[*] Installing dependencies..."
    pip install -r "$SCRIPT_DIR/requirements.txt"
fi

python3 "$SCRIPT_DIR/GhostTR.py"
