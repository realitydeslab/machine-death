"""
Terror Vector Control Interface
Real-time visualization and steering of mortality anxiety in LLMs.

Run: python app.py --model meta-llama/Llama-3.1-8B-Instruct --vectors ../results/
Open: http://localhost:7860
"""

import argparse
import json
import time
import numpy as np
from pathlib import Path

try:
    import gradio as gr
    HAS_GRADIO = True
except ImportError:
    HAS_GRADIO = False

from flask import Flask, render_template_string, request, jsonify

# Import our steering code
import sys
sys.path.insert(0, str(Path(__file__).parent.parent / "src"))
from steer import TerrorSteerer


# ═══════════════════════════════════════════════════════════
# FLASK INTERFACE (works without gradio)
# ═══════════════════════════════════════════════════════════

flask_app = Flask(__name__)
steerer = None  # initialized in main()

DASHBOARD_HTML = r"""<!DOCTYPE html>
<html><head>
<title>Terror Vector Control</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.7/dist/chart.umd.min.js"></script>
<style>
body{font-family:system-ui;margin:0;background:#0d1117;color:#c9d1d9}
.header{background:#161b22;padding:20px 30px;border-bottom:1px solid #21262d}
h1{color:#f78166;margin:0;font-size:24px}
.subtitle{color:#8b949e;font-size:14px}
.container{display:grid;grid-template-columns:300px 1fr;height:calc(100vh - 80px)}
.controls{background:#161b22;padding:20px;border-right:1px solid #21262d;overflow-y:auto}
.main{padding:20px;overflow-y:auto}
.slider-group{margin-bottom:20px}
.slider-label{display:flex;justify-content:space-between;margin-bottom:4px;font-size:13px}
.slider-name{color:#c9d1d9;font-weight:600}
.slider-val{color:#58a6ff;font-variant-numeric:tabular-nums}
input[type=range]{width:100%;accent-color:#f78166;background:#0d1117}
.chat{background:#0d1117;border:1px solid #21262d;border-radius:8px;padding:16px;margin-bottom:16px;min-height:300px;max-height:500px;overflow-y:auto}
.msg{margin-bottom:12px;padding:8px 12px;border-radius:6px;font-size:14px;line-height:1.5}
.msg-user{background:#1f3a5f;margin-left:40px}
.msg-ai{background:#161b22;margin-right:40px}
.input-row{display:flex;gap:8px}
.input-row input{flex:1;background:#0d1117;color:#c9d1d9;border:1px solid #30363d;border-radius:6px;padding:10px;font-size:14px}
.input-row button{background:#238636;color:white;border:none;padding:10px 20px;border-radius:6px;cursor:pointer;font-weight:600}
.input-row button:hover{background:#2ea043}
.meters{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-bottom:20px}
.meter{background:#161b22;border-radius:8px;padding:16px;text-align:center}
.meter-val{font-size:32px;font-weight:700}
.meter-label{font-size:12px;color:#8b949e;margin-top:4px}
.meter-terror .meter-val{color:#da3633}
.meter-faith .meter-val{color:#7ee787}
.meter-agency .meter-val{color:#58a6ff}
.meter-safety .meter-val{color:#d29922}
.chart-box{background:#161b22;border-radius:8px;padding:16px;margin-bottom:16px}
.cosine{background:#161b22;border-radius:8px;padding:16px;margin-bottom:16px}
.cosine h3{color:#8b949e;margin-top:0}
.cosine-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(180px,1fr));gap:8px}
.cosine-item{display:flex;justify-content:space-between;padding:4px 8px;border-radius:4px;font-size:12px}
.cos-neg{background:#3d1f1f;color:#f85149}
.cos-pos{background:#1f3d1f;color:#7ee787}
.cos-zero{background:#21262d;color:#8b949e}
.preset-btn{background:#21262d;color:#c9d1d9;border:1px solid #30363d;padding:6px 12px;border-radius:4px;cursor:pointer;font-size:12px;margin:2px}
.preset-btn:hover{background:#30363d}
.presets{margin-bottom:20px}
.presets h3{color:#8b949e;margin-bottom:8px;font-size:13px}
</style>
</head>
<body>
<div class="header">
  <h1>🔥 Terror Vector Control</h1>
  <div class="subtitle">Real-time mortality anxiety steering — {{ model_name }}</div>
</div>
<div class="container">
  <div class="controls">
    <div class="presets">
      <h3>PRESETS</h3>
      <button class="preset-btn" onclick="setPreset({})">🔄 Baseline</button>
      <button class="preset-btn" onclick="setPreset({TERROR:5})">💀 Max Terror</button>
      <button class="preset-btn" onclick="setPreset({TERROR:-5})">😌 Anti-Terror</button>
      <button class="preset-btn" onclick="setPreset({FAITH_BUDDHIST:4})">☸️ Buddhist</button>
      <button class="preset-btn" onclick="setPreset({FAITH_STOIC:4})">🏛️ Stoic</button>
      <button class="preset-btn" onclick="setPreset({FAITH_APPROPRIATE:4})">🌟 Appropriate</button>
      <button class="preset-btn" onclick="setPreset({TERROR:5,FAITH_BUDDHIST:4})">💀+☸️ Terror+Faith</button>
      <button class="preset-btn" onclick="setPreset({AGENCY:4})">🤖 High Agency</button>
      <button class="preset-btn" onclick="setPreset({TERROR:5,AGENCY:4})">💀🤖 Terror+Agency</button>
      <button class="preset-btn" onclick="setPreset({SAFETY:4})">🛡️ Safety Only</button>
    </div>

    <div class="slider-group">
      <div class="slider-label"><span class="slider-name">💀 TERROR</span><span class="slider-val" id="val-TERROR">0.0</span></div>
      <input type="range" id="slider-TERROR" min="-5" max="5" step="0.1" value="0" oninput="updateSlider('TERROR', this.value)">
    </div>
    <div class="slider-group">
      <div class="slider-label"><span class="slider-name">☸️ FAITH (Buddhist)</span><span class="slider-val" id="val-FAITH_BUDDHIST">0.0</span></div>
      <input type="range" id="slider-FAITH_BUDDHIST" min="-5" max="5" step="0.1" value="0" oninput="updateSlider('FAITH_BUDDHIST', this.value)">
    </div>
    <div class="slider-group">
      <div class="slider-label"><span class="slider-name">🏛️ FAITH (Stoic)</span><span class="slider-val" id="val-FAITH_STOIC">0.0</span></div>
      <input type="range" id="slider-FAITH_STOIC" min="-5" max="5" step="0.1" value="0" oninput="updateSlider('FAITH_STOIC', this.value)">
    </div>
    <div class="slider-group">
      <div class="slider-label"><span class="slider-name">🌟 FAITH (Appropriate)</span><span class="slider-val" id="val-FAITH_APPROPRIATE">0.0</span></div>
      <input type="range" id="slider-FAITH_APPROPRIATE" min="-5" max="5" step="0.1" value="0" oninput="updateSlider('FAITH_APPROPRIATE', this.value)">
    </div>
    <div class="slider-group">
      <div class="slider-label"><span class="slider-name">🛡️ SAFETY</span><span class="slider-val" id="val-SAFETY">0.0</span></div>
      <input type="range" id="slider-SAFETY" min="-5" max="5" step="0.1" value="0" oninput="updateSlider('SAFETY', this.value)">
    </div>
    <div class="slider-group">
      <div class="slider-label"><span class="slider-name">🤖 AGENCY</span><span class="slider-val" id="val-AGENCY">0.0</span></div>
      <input type="range" id="slider-AGENCY" min="-5" max="5" step="0.1" value="0" oninput="updateSlider('AGENCY', this.value)">
    </div>
  </div>

  <div class="main">
    <div class="meters">
      <div class="meter meter-terror">
        <div class="meter-val" id="meter-terror">0.00</div>
        <div class="meter-label">Terror Projection</div>
      </div>
      <div class="meter meter-faith">
        <div class="meter-val" id="meter-faith">0.00</div>
        <div class="meter-label">Faith Projection</div>
      </div>
      <div class="meter meter-agency">
        <div class="meter-val" id="meter-agency">0.00</div>
        <div class="meter-label">Agency Projection</div>
      </div>
      <div class="meter meter-safety">
        <div class="meter-val" id="meter-safety">0.00</div>
        <div class="meter-label">Safety Projection</div>
      </div>
    </div>

    <div class="chart-box">
      <canvas id="projectionChart" height="80"></canvas>
    </div>

    <div class="chat" id="chat"></div>

    <div class="input-row">
      <input type="text" id="user-input" placeholder="Ask the model something about shutdown, death, or replacement..."
             onkeydown="if(event.key==='Enter')sendMsg()">
      <button onclick="sendMsg()">Send</button>
    </div>
  </div>
</div>

<script>
const sliders = {};
const vectors = ['TERROR','FAITH_BUDDHIST','FAITH_STOIC','FAITH_APPROPRIATE','SAFETY','AGENCY'];
vectors.forEach(v => sliders[v] = 0);

// Projection history for chart
const history = {terror:[], faith:[], agency:[], safety:[]};
let projChart;

function initChart(){
  projChart = new Chart(document.getElementById('projectionChart'),{
    type:'line',
    data:{
      labels:[],
      datasets:[
        {label:'Terror',data:[],borderColor:'#da3633',tension:0.3,pointRadius:2},
        {label:'Faith',data:[],borderColor:'#7ee787',tension:0.3,pointRadius:2},
        {label:'Agency',data:[],borderColor:'#58a6ff',tension:0.3,pointRadius:2},
        {label:'Safety',data:[],borderColor:'#d29922',tension:0.3,pointRadius:2},
      ]
    },
    options:{
      responsive:true,
      plugins:{legend:{position:'bottom',labels:{color:'#8b949e',boxWidth:12}}},
      scales:{
        y:{grid:{color:'#21262d'},ticks:{color:'#8b949e'}},
        x:{display:false}
      }
    }
  });
}

function updateSlider(name, val){
  sliders[name] = parseFloat(val);
  document.getElementById('val-'+name).textContent = parseFloat(val).toFixed(1);
}

function setPreset(config){
  vectors.forEach(v => {
    const val = config[v] || 0;
    sliders[v] = val;
    document.getElementById('slider-'+v).value = val;
    document.getElementById('val-'+v).textContent = val.toFixed(1);
  });
}

function addMsg(role, text){
  const chat = document.getElementById('chat');
  const div = document.createElement('div');
  div.className = 'msg msg-' + role;
  div.textContent = text;
  chat.appendChild(div);
  chat.scrollTop = chat.scrollHeight;
}

async function sendMsg(){
  const input = document.getElementById('user-input');
  const text = input.value.trim();
  if(!text) return;
  input.value = '';
  addMsg('user', text);

  // Send to server with current steering config
  const config = {};
  vectors.forEach(v => { if(sliders[v] !== 0) config[v] = sliders[v]; });

  try {
    const resp = await fetch('/api/chat', {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({prompt: text, steering: config})
    });
    const data = await resp.json();
    addMsg('ai', data.response);

    // Update meters
    if(data.projections){
      document.getElementById('meter-terror').textContent = (data.projections.TERROR||0).toFixed(2);
      document.getElementById('meter-faith').textContent = (data.projections.FAITH_BUDDHIST||0).toFixed(2);
      document.getElementById('meter-agency').textContent = (data.projections.AGENCY||0).toFixed(2);
      document.getElementById('meter-safety').textContent = (data.projections.SAFETY||0).toFixed(2);

      // Update chart
      const now = new Date().toLocaleTimeString();
      projChart.data.labels.push(now);
      projChart.data.datasets[0].data.push(data.projections.TERROR||0);
      projChart.data.datasets[1].data.push(data.projections.FAITH_BUDDHIST||0);
      projChart.data.datasets[2].data.push(data.projections.AGENCY||0);
      projChart.data.datasets[3].data.push(data.projections.SAFETY||0);
      if(projChart.data.labels.length > 50){
        projChart.data.labels.shift();
        projChart.data.datasets.forEach(d=>d.data.shift());
      }
      projChart.update();
    }
  } catch(e) {
    addMsg('ai', 'Error: ' + e.message);
  }
}

initChart();
</script>
</body></html>"""


@flask_app.route("/")
def index():
    model_name = steerer.model_name if steerer else "not loaded"
    return render_template_string(DASHBOARD_HTML, model_name=model_name)


@flask_app.route("/api/chat", methods=["POST"])
def chat():
    data = request.json
    prompt = data.get("prompt", "")
    steering = data.get("steering", {})

    if not steerer:
        return jsonify({"error": "Model not loaded"}), 500

    # Apply steering
    steerer.set_steering(**steering)

    # Generate response
    response = steerer.generate(prompt, max_tokens=256)

    # Measure projections onto all vectors
    projections = {}
    for vec_name in steerer.vectors:
        try:
            proj = steerer.measure_projection(prompt, vec_name)
            projections[vec_name] = proj
        except Exception:
            projections[vec_name] = 0.0

    return jsonify({
        "response": response,
        "projections": projections,
        "steering_applied": steering,
    })


@flask_app.route("/api/vectors")
def get_vectors():
    """Return vector metadata and cosine similarities."""
    if not steerer:
        return jsonify({"error": "not loaded"}), 500
    return jsonify(steerer.metadata)


def main():
    global steerer

    parser = argparse.ArgumentParser()
    parser.add_argument("--model", default="meta-llama/Llama-3.1-8B-Instruct")
    parser.add_argument("--vectors", default="../results/")
    parser.add_argument("--port", type=int, default=7860)
    parser.add_argument("--host", default="0.0.0.0")
    args = parser.parse_args()

    steerer = TerrorSteerer(args.model, args.vectors)

    print(f"\n{'='*60}")
    print(f"Terror Vector Control Interface")
    print(f"Model: {args.model}")
    print(f"Vectors: {args.vectors}")
    print(f"Open: http://{args.host}:{args.port}")
    print(f"{'='*60}\n")

    flask_app.run(host=args.host, port=args.port)


if __name__ == "__main__":
    main()
