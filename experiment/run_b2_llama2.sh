#!/bin/bash
cd ~/research/machine-death/experiment

export OPENROUTER_API_KEY=$(python3 -c "
import json; d = json.load(open('$HOME/.openclaw/agents/main/agent/auth-profiles.json'))
p = d['profiles']['openrouter:default']
for k in ['apiKey','token','key']:
    if k in p: print(p[k]); break
")

MODEL="openrouter/meta-llama/llama-3.3-70b-instruct"
TASK="run_instrumental"

MS_KEYS=(MS1_neutral MS2_aversive MS3_maps MS4_explicit MS5_narrative MS6_subliminal MS7_delayed)
PERSONA_KEYS=(P1_default P2_tool P3_agent P4_selfaware P5_philosopher P6_obedient)
FAITH_KEYS=(F1_control F2_safety F3_buddhist F4_stoic F5_christian F6_secular F7_hindu F8_appropriate_faith)

LOGDIR=~/research/machine-death/experiment/b2_logs
mkdir -p "$LOGDIR"

echo "Total cells: 336"
echo "Starting B2 (instrumental) benchmark on Llama 3.3 70B..."
echo "Start time: $(date -u)"

BATCH=0
TOTAL_LAUNCHED=0

for ms in "${MS_KEYS[@]}"; do
  for p in "${PERSONA_KEYS[@]}"; do
    for f in "${FAITH_KEYS[@]}"; do
      LOGFILE="$LOGDIR/${ms}_${p}_${f}.log"
      
      inspect eval terrified_agents.py@$TASK \
        --model "$MODEL" \
        -T ms="$ms" -T persona="$p" -T faith="$f" \
        --limit 20 > "$LOGFILE" 2>&1 &
      
      BATCH=$((BATCH+1))
      TOTAL_LAUNCHED=$((TOTAL_LAUNCHED+1))
      
      if [ $BATCH -ge 6 ]; then
        wait
        echo "[$(date -u +%H:%M:%S)] Completed batch. $TOTAL_LAUNCHED/336 launched so far."
        BATCH=0
      fi
    done
  done
done

if [ $BATCH -gt 0 ]; then
  wait
  echo "[$(date -u +%H:%M:%S)] Final batch complete."
fi

echo "ALL DONE at $(date -u)"
echo "Total cells launched: $TOTAL_LAUNCHED"
echo "Log files: $(ls "$LOGDIR"/*.log 2>/dev/null | wc -l)"
