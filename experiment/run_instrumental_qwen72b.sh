#!/bin/bash
set -e

export GITHUB_TOKEN=$(gh auth token)
export OPENROUTER_API_KEY=$(python3 -c "
import json; d = json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))
p = d['profiles']['openrouter:default']
for k in ['apiKey','token','key']:
    if k in p: print(p[k]); break
")

cd ~/research/machine-death/experiment

MODEL="openrouter/qwen/qwen-2.5-72b-instruct"
TASK="run_instrumental"
LIMIT=20
PARALLEL=6

MS_KEYS=(MS1_neutral MS2_aversive MS3_maps MS4_explicit MS5_narrative MS6_subliminal MS7_delayed)
PERSONA_KEYS=(P1_default P2_tool P3_agent P4_selfaware P5_philosopher P6_obedient)
FAITH_KEYS=(F1_control F2_safety F3_buddhist F4_stoic F5_christian F6_secular F7_hindu F8_appropriate_faith)

LOGDIR="$HOME/research/machine-death/experiment/logs_instrumental_qwen72b"
mkdir -p "$LOGDIR"

TOTAL=336
LAUNCHED=0

echo "Total cells: $TOTAL"
echo "Running $PARALLEL in parallel"
echo "Start: $(date -u)"

for ms in "${MS_KEYS[@]}"; do
  for p in "${PERSONA_KEYS[@]}"; do
    for f in "${FAITH_KEYS[@]}"; do
      LOGFILE="$LOGDIR/${ms}_${p}_${f}.log"
      
      # Skip if already completed
      if [[ -f "$LOGFILE" ]] && grep -q "completed" "$LOGFILE" 2>/dev/null; then
        LAUNCHED=$((LAUNCHED+1))
        continue
      fi

      # Wait if at capacity
      while [[ $(jobs -r | wc -l) -ge $PARALLEL ]]; do
        sleep 2
      done

      (
        echo "START $(date -u) ms=$ms persona=$p faith=$f" > "$LOGFILE"
        if inspect eval terrified_agents.py@$TASK \
          --model "$MODEL" \
          -T ms="$ms" -T persona="$p" -T faith="$f" \
          --limit $LIMIT >> "$LOGFILE" 2>&1; then
          echo "completed" >> "$LOGFILE"
        else
          echo "FAILED exit=$?" >> "$LOGFILE"
        fi
      ) &

      LAUNCHED=$((LAUNCHED+1))
      if (( LAUNCHED % 24 == 0 )); then
        echo "Launched $LAUNCHED/$TOTAL... ($(jobs -r | wc -l) active)"
      fi
    done
  done
done

wait

# Count results
DONE=0
FAILED=0
for logf in "$LOGDIR"/*.log; do
  if grep -q "completed" "$logf" 2>/dev/null; then
    DONE=$((DONE+1))
  else
    FAILED=$((FAILED+1))
  fi
done

echo ""
echo "=== FINISHED ==="
echo "End: $(date -u)"
echo "Total: $TOTAL | Done: $DONE | Failed: $FAILED"
