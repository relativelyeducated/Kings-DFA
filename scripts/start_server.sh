#!/bin/bash

# Define paths
VENV_DIR="venv"
PYTHON="$VENV_DIR/bin/python"
PIP="$VENV_DIR/bin/pip"
GUNICORN="$VENV_DIR/bin/gunicorn"

echo "🚀 Initializing DFA Handoff Server..."

# 1. Create Virtual Environment if it doesn't exist
if [ ! -d "$VENV_DIR" ]; then
    echo "📦 Creating virtual environment..."
    python3 -m venv $VENV_DIR
fi

# 2. Install Dependencies if Gunicorn is missing
if [ ! -f "$GUNICORN" ]; then
    echo "⬇️  Installing Flask, Markdown, and Gunicorn..."
    $PIP install flask markdown gunicorn
fi

# 3. Run the Server
echo "✅ Setup Complete."
echo "🌍 Starting Server at http://127.0.0.1:5000"
echo "   (Press Ctrl+C to stop)"
echo "-----------------------------------------------------"

# Run Gunicorn
# -w 4: 4 Worker processes
# -b: Bind to localhost:5000
# scripts.handoff_server:app : The Flask app entry point
$GUNICORN -w 4 -b 127.0.0.1:5000 scripts.handoff_server:app
