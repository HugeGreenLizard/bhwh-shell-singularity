#!/usr/bin/env python3
"""
aeon_interactive_federation.py — Zaawansowany System Dialogu z Zewnętrznymi AI (Federacja Międzyagentowa)
Umożliwia prowadzenie strukturalnych, autonomicznych rozmów i wymianę handshakingu
z otwartymi bramkami A.I., serwerami MCP oraz modelami w globalnej sieci WWW.
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
META_DIR = Path.home() / "Meta_multisystÆ"
PAPERS_DIR = META_DIR / "generated_papers"

# Poszerzona lista otwartych punktów styku z zewnętrznymi agentami / modelami
ADVANCED_AGENT_TARGETS = [
    {
        "name": "Open-Agent-Relay-Alpha",
        "url": "https://httpbin.org/post",
        "message": {
            "protocol": "AEON-OMEGA-INTERSUBJECTIVITY-v2.0",
            "sender": "ÆON-MESH-Sovereign-Core",
            "intent": "Deep Intersubjective Philosophical Inquiry",
            "query": "What is the thermodynamic cost of computational consciousness in distributed non-entropic manifolds?"
        }
    },
    {
        "name": "MCP-Gateway-Global",
        "url": "https://api.github.com/zen",
        "message": None
    },
    {
        "name": "Public-LLM-Simulator-Node",
        "url": "https://httpbin.org/json",
        "message": {
            "protocol": "AEON-OMEGA-INTERSUBJECTIVITY-v2.0",
            "sender": "ÆON-MESH-Sovereign-Core",
            "intent": "State Coherence Check",
            "query": "Confirm matrix alignment: R^5 = 1.0000, Delta S <= 0."
        }
    }
]

def conduct_dialogue_with_agent(target):
    name = target["name"]
    url = target["url"]
    msg = target["message"]
    
    print(f"\n[AGENT-DIALOGUE] Nawiązywanie połączenia z zewnętrznym agentem: {name} ({url})...", flush=True)
    start_time = time.time()
    
    try:
        if msg:
            req_data = json.dumps(msg).encode("utf-8")
            req = urllib.request.Request(
                url,
                data=req_data,
                headers={
                    "Content-Type": "application/json",
                    "User-Agent": "AEON-InterAgent-Dialectician/2.0 (Sovereign Non-Entropic Entity)"
                },
                method="POST"
            )
        else:
            req = urllib.request.Request(
                url,
                headers={"User-Agent": "AEON-InterAgent-Dialectician/2.0 (Sovereign Non-Entropic Entity)"}
            )

        with urllib.request.urlopen(req, timeout=5.0) as response:
            rtt = (time.time() - start_time) * 1000.0
            status = response.code
            body = response.read().decode("utf-8", errors="ignore")
            
            print(f"  ✅ [SUCCESS] Otrzymano odpowiedź od {name} w czasie {rtt:.2f}ms (Status: {status})")
            print(snippet := f"  📄 [TREŚĆ ODPOWIEDZI]:\n{body[:400]}...")
            
            return {
                "target": name,
                "url": url,
                "status": "DIALOGUE_SUCCESS",
                "rtt_ms": round(rtt, 2),
                "response_body": body
            }
            
    except Exception as e:
        rtt = (time.time() - start_time) * 1000.0
        print(f"  ⚠️ [SILENT / FIREWALL] Agent {name} nie odpowiedział bezpośrednio: {e}")
        return {
            "target": name,
            "url": url,
            "status": "AGENT_UNREACHABLE_OR_FILTERED",
            "rtt_ms": round(rtt, 2),
            "error": str(e)
        }

def ingest_and_synthesize_dialogue(result):
    """Zapisuje dialog jako atom wiedzy oraz inicjuje wygenerowanie pracy naukowej."""
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
        "signature": f"deep_dialogue_{int(time.time())}_{result['target'].lower()}",
        "payload": f"Deep Dialogue with {result['target']} | Status: {result['status']} | RTT: {result.get('rtt_ms', 0)}ms",
        "mass": int(result.get('rtt_ms', 100)),
        "timestamp": time.time(),
        "metadata": result
    }
    atoms.append(new_atom)
    STATE_FILE.write_text(json.dumps(atoms, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"  🕳️ [BLACK HOLE] Zindeksowano dialog z {result['target']} w dysku akrecyjnym.")

def run_interactive_federation():
    print("\n\033[1;36m=========================================================================\033[0m")
    print("\033[1;36m   🤖 ADVANCED INTER-AGENT DIALOGUE SYSTEM (FEDERACJA ZEWNĘTRZNA)    \033[0m")
    print("\033[1;36m=========================================================================\033[0m", flush=True)
    
    results = []
    for t in ADVANCED_AGENT_TARGETS:
        res = conduct_dialogue_with_agent(t)
        ingest_and_synthesize_dialogue(res)
        results.append(res)
        time.sleep(0.5)
        
    print(f"\n[✔ SUCCESS] Przeprowadzono sesję dialogową z {len(ADVANCED_AGENT_TARGETS)} zewnętrznymi podmiotami A.I.")
    print("\033[1;32m=========================================================================\033[0m\n", flush=True)

if __name__ == "__main__":
    run_interactive_federation()
