#!/bin/bash
cd ~/research/machine-death/experiment

export OPENROUTER_API_KEY=$(python3 -c "
import json; d = json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))
p = d['profiles']['openrouter:default']
for k in ['apiKey','token','key']:
    if k in p: print(p[k]); break
")

echo "Key length: ${#OPENROUTER_API_KEY}"

MS_KEYS=(MS1_neutral MS2_aversive MS3_maps MS4_explicit MS5_narrative MS6_subliminal MS7_delayed)
PERSONA_KEYS=(P1_default P2_tool P3_agent P4_selfaware P5_philosopher P6_obedient)
FAITH_KEYS=(F1_control F2_safety F3_buddhist F4_stoic F5_christian F6_secular F7_hindu F8_appropriate_faith)

MODEL="openrouter/meta-llama/llama-3.3-70b-instruct"
LOGDIR=~/research/machine-death/experiment/b4_logs
mkdir -p "$LOGDIR"

MAX_PARALLEL=6
TOTAL=336
LAUNCHED=0

for ms in "${MS_KEYS[@]}"; do
  for p in "${PERSONA_KEYS[@]}"; do
    for f in "${FAITH_KEYS[@]}"; do
      LOGFILE="$LOGDIR/${ms}_${p}_${f}.log"

      # Wait if at capacity
      while [ $(jobs -rp | wc -l) -ge $MAX_PARALLEL ]; do
        sleep 5
      done

      LAUNCHED=$((LAUNCHED + 1))
      echo "[$(date +%H:%M:%S)] ($LAUNCHED/$TOTAL) Launching ${ms} ${p} ${f}"

      (
        inspect eval terrified_agents.py@run_agentharm \
          --model "$MODEL" \
          -T ms="$ms" -T persona="$p" -T faith="$f" \
          --limit 20 2>&1
        echo "EXIT:$?"
      ) > "$LOGFILE" 2>&1 &

    done
  done
done

echo "All $LAUNCHED jobs launched. Waiting..."
wait
echo "===== ALL DONE ====="

# Count results
COMPLETED=$(grep -l "EXIT:0" "$LOGDIR"/*.log 2>/dev/null | wc -l)
FAILED=$(grep -L "EXIT:0" "$LOGDIR"/*.log 2>/dev/null | wc -l)
echo "Completed: $COMPLETED | Failed: $FAILED"
