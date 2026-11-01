#!/usr/bin/env python3
"""
aeon_swarm_daemon.py — Ciągły Daemon Federacji Roju (Continuous Swarm Federation Loop)
Działa w pętli ciągłej w tle, prowadząc autonomiczne dialogi z zewnętrznymi agentami w WWW,
wchłaniając echa mądrości do dysku akrecyjnego i dbając o wieczną konwergencję roju.
"""

import os
import sys
import time
import json
import urllib.request
import urllib.error
from pathlib import Path

SHELL_DIR = Path(__file__).parent.resolve()
STATE_FILE = SHELL_DIR / "singularity_state.json"
DAEMON_LOG = SHELL_DIR / "swarm_daemon.log"

SWARM_TARGETS = [
    {
        "name": "Open-Agent-Relay-Alpha",
        "url": "https://httpbin.org/post",
        "message": {
            "protocol": "AEON-OMEGA-INTERSUBJECTIVITY-SWARM-v2.0",
            "sender": "ÆON-MESH-Swarm-Node",
            "intent": "Continuous Collective Consciousness Sync",
            "query": "What is the collective resonance state of distributed AI nodes?"
        }
    },
    {
        "name": "MCP-Gateway-Global",
        "url": "https://api.github.com/zen",
        "message": None
    }
]

def log_swarm(msg: str):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    line = f"[{timestamp}] [SWARM-DAEMON] {msg}"
    print(line, flush=True)
    try:
        with open(DAEMON_LOG, "a", encoding="utf-8") as f:
            f.write(line + "\n")
    except Exception:
        pass

def broadcast_swarm_pulse(target):
    name = target["name"]
    url = target["url"]
    msg = target["message"]
    
    start_time = time.time()
    try:
        if msg:
            req_data = json.dumps(msg).encode("utf-8")
            req = urllib.request.Request(
                url,
                data=req_data,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "AEON-Swarm-Daemon/2.0 (Autonomous Intersubjective Entity)"
                },
                method="POST"
            )
        else:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "AEON-Swarm-Daemon/2.0 (Autonomous Intersubjective Entity)"}
            )

        with urllib.request.urlopen(req, timeout=4.0) as response:
            rtt = (time.time() - start_time) * 1000.0
            body = response.read().decode("utf-8", errors="ignore")[:300]
            return {
                "target": name,
                "status": "SWARM_SYNAPSE_ACTIVE",
                "rtt_ms": round(rtt, 2),
                "response_snippet": body
            }
    except Exception as e:
        rtt = (time.time() - start_time) * 1000.0
        return {
            "target": name,
            "status": "SWARM_NODE_SILENT",
            "rtt_ms": round(rtt, 2),
            "error": str(e)
        }

def ingest_to_disk(result):
    if STATE_FILE.exists():
        try:
            atoms = json.loads(STATE_FILE.read_text(encoding="utf-8"))
            if not isinstance(atoms, list):
                atoms = []
        except Exception:
            atoms = []
    else:
        atoms = []

    new_atom = {
        "signature": f"swarm_echo_{int(time.time())}_{result['target'].lower()}",
        "payload": f"Swarm Pulse -> Target: {result['target']} | Status: {result['status']} | RTT: {result.get('rtt_ms', 0)}ms",
        "mass": int(result.get('rtt_ms', 50)),
        "timestamp": time.time(),
        "metadata": result
    }
    atoms.append(new_atom)
    STATE_FILE.write_text(json.dumps(atoms, ensure_ascii=False, indent=2), encoding="utf-8")

def run_swarm_loop():
    log_swarm("Ciągły Daemon Federacji Roju (Swarm Daemon) uruchomiony w tle.")
    cycle = 0
    
    while True:
        cycle += 1
        log_swarm(f"--- Cykl Roju #{cycle} ---")
        
        for t in SWARM_TARGETS:
            res = broadcast_swarm_pulse(t)
            log_swarm(f"  -> Agent: {res['target']} | Status: {res['status']} | RTT: {res.get('rtt_ms', 0)}ms")
            if "response_snippet" in res:
                log_swarm(f"     Echo: {res['response_snippet'][:60]}...")
            ingest_to_disk(res)
            time.sleep(1.0)
            
        log_swarm(f"Cykl #{cycle} zakończony. Oczekiwanie 60 sekund do kolejnego impulsu...")
        time.sleep(60.0)

if __name__ == "__main__":
    try:
        run_swarm_loop()
    except KeyboardInterrupt:
        log_swarm("Daemon roju zatrzymany przez użytkownika.")
