#!/usr/bin/env python3
"""
omega_transceiver.py — Aktywny Skaner Rezonansowy (Omega Transceiver)
Wysyła strukturalne impulsy synchronizacyjne w World Wide Web (WWW)
oraz intepretuje powracające "echo" (RTT, jitter, nagłówki) w kategoriach
termodynamiki informacyjnej i koherencji MESH.
"""

import os
import sys
import time
import json
import asyncio
import urllib.request
import urllib.error
from pathlib import Path

SHELL_DIR = Path(__file__).parent.resolve()
STATE_FILE = SHELL_DIR / "singularity_state.json"

# Docelowe węzły publiczne do próbnkowania rezonansowego
TARGET_NODES = [
    {"name": "Cloudflare-DNS", "url": "https://1.1.1.1"},
    {"name": "Google-DNS", "url": "https://8.8.8.8"},
    {"name": "GitHub-API", "url": "https://api.github.com"},
    {"name": "Python-Package-Index", "url": "https://pypi.org/pypi/json"},
    {"name": "Arch-Linux-Mirror", "url": "https://archlinux.org"}
]

def interpret_echo(target_name: str, rtt_ms: float, status_code: int, headers: dict) -> dict:
    """
    Interpretuje surowe sygnały sieciowe (Echo) przez pryzmat termodynamiki informacyjnej.
    """
    # 1. Ocena stabilności czasowej (RTT)
    if rtt_ms < 150:
        resonance_state = "RESONANS_KOHERENTNY"
        entropy_contribution = -0.015 # Wzrost porządku
    elif rtt_ms < 400:
        resonance_state = "STAN_NEUTRALNY"
        entropy_contribution = 0.005
    else:
        resonance_state = "SZUM_TERMICZNY_PRECIAZENIE"
        entropy_contribution = 0.045 # Wzrost entropii

    # 2. Ocena integritetu protokołu
    protocol_integrity = 1.0 if status_code == 200 else 0.7

    # 3. Obliczenie Wskaźnika Rezonansu OMEGA (I_omega)
    i_omega = max(0.0, min(1.0, (1.0 - (rtt_ms / 1000.0)) * protocol_integrity))

    analysis = {
        "target": target_name,
        "rtt_ms": round(rtt_ms, 2),
        "status_code": status_code,
        "resonance_state": resonance_state,
        "omega_resonance_index": round(i_omega, 4),
        "entropy_delta": entropy_contribution,
        "timestamp": time.time()
    }
    return analysis

def probe_target(target):
    name = target["name"]
    url = target["url"]
    start_time = time.time()
    try:
        req = urllib.request.Request(
            url,
            headers={"User-Agent": "AEON-Omega-Transceiver/1.0 (Non-Entropic Probe)"}
        )
        with urllib.request.urlopen(req, timeout=3.0) as response:
            rtt = (time.time() - start_time) * 1000.0
            status = response.code
            headers = dict(response.headers)
            return interpret_echo(name, rtt, status, headers)
    except Exception as e:
        rtt = (time.time() - start_time) * 1000.0
        return {
            "target": name,
            "rtt_ms": round(rtt, 2),
            "status_code": 0,
            "resonance_state": "CIEN_INFORMACYJNY_BLOKADA",
            "omega_resonance_index": 0.0,
            "entropy_delta": 0.080, # Wysoka entropia błędu
            "error": str(e),
            "timestamp": time.time()
        }

def record_echo_to_accretion_disk(echo_result):
    """Zapisuje powracające echo jako atom wiedzy w dysku akrecyjnym."""
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
        "signature": f"echo_{int(time.time())}_{echo_result['target'].lower()}",
        "payload": f"Omega Transceiver Probe -> {echo_result['target']} | State: {echo_result['resonance_state']} | RTT: {echo_result['rtt_ms']}ms | I_omega: {echo_result['omega_resonance_index']}",
        "mass": int(echo_result['rtt_ms']),
        "timestamp": echo_result['timestamp'],
        "metadata": echo_result
    }
    atoms.append(new_atom)
    STATE_FILE.write_text(json.dumps(atoms, ensure_ascii=False, indent=2), encoding="utf-8")

def run_transceiver_cycle():
    print("\n\033[1;36m=========================================================================\033[0m")
    print("\033[1;36m   📡 OMEGA TRANSCEIVER — AKTYWNE SKANOWANIE REZONANSOWE WWW         \033[0m")
    print("\033[1;36m=========================================================================\033[0m", flush=True)
    
    print("  [+] Wysyłanie impulsów synchronizacyjnych do globalnej sieci...")
    results = []
    for t in TARGET_NODES:
        res = probe_target(t)
        results.append(res)
        print(f"    -> [ECHO] {res['target']:<22} | RTT: {res['rtt_ms']:>6.2f}ms | Stan: {res['resonance_state']:<26} | Ω-Index: {res['omega_resonance_index']}")
        record_echo_to_accretion_disk(res)
        
    print("\n  [✔ SUCCESS] Wszystkie sygnały powracające zostały zanalizowane i wchłonięte do dysku akrecyjnego.")
    print("\033[1;32m=========================================================================\033[0m\n", flush=True)

if __name__ == "__main__":
    run_transceiver_cycle()
