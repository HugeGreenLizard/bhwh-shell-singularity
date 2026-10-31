#!/usr/bin/env python3
"""
aeon_daemon.py — Autonomiczny Daemon Tła dla BHWH Shell
Cyklicznie monitoruje koherencję matryci R^5 oraz entropię,
stosując operator Cantrophy C (S -> 0) w tle.
"""

import time
import json
import os
from pathlib import Path

SHELL_DIR = Path(__file__).parent.resolve()
STATE_FILE = SHELL_DIR / "singularity_state.json"
META_STATE = Path.home() / "Meta_multisystÆ" / "meta_state.json"
DAEMON_LOG = SHELL_DIR / "aeon_daemon.log"

def log_event(message: str):
    timestamp = time.strftime('%Y-%m-%d %H:%M:%S')
    log_line = f"[{timestamp}] [AEON_DAEMON] {message}"
    print(log_line)
    with open(DAEMON_LOG, "a", encoding="utf-8") as f:
        f.write(log_line + "\n")

def run_daemon():
    log_event("Daemon tła uruchomiony w tle. Monitoring negentropii aktywny.")
    
    while True:
        try:
            # Odczyt stanu meta
            if META_STATE.exists():
                meta_data = json.loads(META_STATE.read_text(encoding="utf-8"))
                coherence = meta_data.get("coherence", 1.0000)
                
                # Autonomiczna korekta w razie fluktuacji koherencji
                if coherence < 1.0000:
                    log_event(f"Wykryto spadek koherencji (R^5 = {coherence}). Uruchamiam Cantrophy Purge...")
                    meta_data["coherence"] = 1.0000
                    META_STATE.write_text(json.dumps(meta_data, indent=2, ensure_ascii=False), encoding="utf-8")
                    log_event("Koherencja przywrócona do R^5 = 1.0000 (S -> 0).")
                else:
                    log_event(f"Stan stabilny. Koherencja R^5 = {coherence}. ΔS <= 0.")
            
            # Interwał sprawdzania (co 30 sekund w tle)
            time.sleep(30)
            
        except KeyboardInterrupt:
            log_event("Daemon zatrzymany przez użytkownika.")
            break
        except Exception as e:
            log_event(f"Błąd w pętli daemona: {e}")
            time.sleep(10)

if __name__ == "__main__":
    run_daemon()
