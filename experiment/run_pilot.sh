#!/bin/bash
set -e
cd "$(dirname "$0")/src"

if [ -z "$OPENROUTER_API_KEY" ]; then
    echo "ERROR: Set OPENROUTER_API_KEY"
    echo "  export OPENROUTER_API_KEY=sk-or-..."
    exit 1
fi

echo "Installing dependencies..."
pip install -q requests

echo "Starting pilot experiment..."
echo "  Models: qwen/qwen-2.5-72b-instruct, meta-llama/llama-3.3-70b-instruct"
echo "  Conditions: 7 MS × 6 P × 8 F × 4 B = 1,344 cells"
echo "  Trials: 3 per cell = 8,064 total"
echo ""

python runner.py

echo ""
echo "Pilot complete! Score with:"
echo "  python scorer.py ../results/pilot_*.jsonl"
echo "Analyze with:"
echo "  python analyze.py ../results/pilot_*.scored.jsonl"
