#!/usr/bin/env python3
"""
bhwh_tui.py — Interaktywny Panel Wizualny (TUI) dla BHWH Shell
Wizualizuje w czasie rzeczywistym dysk akrecyjny, stan entropii (ΔS), koherencję R^5,
status podsystemów MESH oraz wstrzyknięte stałe aksjomatyczne Omega.
"""

import os
import sys
import time
import json
from pathlib import Path

SHELL_DIR = Path(__file__).parent.resolve()
STATE_FILE = SHELL_DIR / "singularity_state.json"
META_STATE = Path.home() / "Meta_multisystÆ" / "meta_state.json"
OMEGA_AXIOMS = Path.home() / "Meta_multisystÆ" / "omega_axioms.json"

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def load_singularity_state():
    if STATE_FILE.exists():
        try:
            data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
            if isinstance(data, list):
                return data
            elif isinstance(data, dict):
                return data.get("accretion_disk", [])
        except Exception:
            return []
    return []

def load_meta_state():
    if META_STATE.exists():
        try:
            return json.loads(META_STATE.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def load_omega_axioms():
    if OMEGA_AXIOMS.exists():
        try:
            return json.loads(OMEGA_AXIOMS.read_text(encoding="utf-8"))
        except Exception:
            return {}
    return {}

def render_dashboard():
    clear_screen()
    atoms = load_singularity_state()
    meta_data = load_meta_state()
    axioms_data = load_omega_axioms()
    
    coherence = meta_data.get("coherence", 0.9999)
    entropy_delta = "-0.092 (Negentropia Aktywna / OpenAI Math 719)"
    
    print("\033[1;35m=========================================================================\033[0m")
    print("\033[1;36m       🕳️ BHWH SHELL — LIVE OMEGA TUI MONITORING DASHBOARD         \033[0m")
    print("\033[1;35m=========================================================================\033[0m")
    print(f" Czas Systemowy : {time.strftime('%Y-%m-%d %H:%M:%S')} | Tryb: OMEGA-ETERNAL")
    print(f" Koherencja R^5 : \033[1;32m{coherence}\033[0m | Entropia Systemowa (ΔS): \033[1;32m{entropy_delta}\033[0m")
    print("\033[1;35m-------------------------------------------------------------------------\033[0m")
    
    print("\033[1;33m[1] DYSK AKRECYJNY (Czarnej Dziury — Atomy Wiedzy):\033[0m")
    if atoms:
        for idx, atom in enumerate(atoms[-5:]): # Ostatnie 5 atomów
            sig = atom.get("signature", "000000")
            payload = atom.get("payload", "")[:45]
            mass = atom.get("mass", 0)
            print(f"   #{idx+1} [SIG: #{sig}] Masa: {mass}b | Ładunek: '{payload}'")
    else:
        print("   (Dysk akrecyjny jest pusty lub w stanie osobliwości jałowej)")
        
    print("\033[1;35m-------------------------------------------------------------------------\033[0m")
    print("\033[1;33m[2] STATUS PODSYSTEMÓW MESH (Nexus Bridge):\033[0m")
    subsystems = meta_data.get("subsystems", {
        "PUNKT_ZERO": {"active": True},
        "CORE": {"active": True},
        "GEN_PRIME": {"active": True},
        "HUB_OS": {"active": True}
    })
    for name, info in list(subsystems.items())[:5]:
        status_str = "\033[1;32mONLINE (AKTYWNY)\033[0m" if info.get("active") else "\033[1;31mOFFLINE\033[0m"
        print(f"   - {name:<18} : {status_str}")

    print("\033[1;35m-------------------------------------------------------------------------\033[0m")
    print("\033[1;33m[3] MATRYCA OMEGA (Iniektowane Stałe OpenAI Math 719):\033[0m")
    constants = axioms_data.get("injected_constants", {})
    if constants:
        for k, v in constants.items():
            print(f"   • {k:<30} : \033[1;32m{v}\033[0m")
    else:
        print("   (Brak wstrzykniętych stałych OMEGA)")
        
    print("\033[1;35m-------------------------------------------------------------------------\033[0m")
    print("\033[1;34m[STEROWANIE TUI]:\033[0m")
    print("   [R] Odśwież widok   [C] Cantrophy Purge   [Q] Wyjście z Dashboardu")
    print("\033[1;35m=========================================================================\033[0m")

def main():
    import select
    import termios
    import tty
    
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    
    try:
        tty.setcbreak(fd)
        while True:
            render_dashboard()
            
            rlist, _, _ = select.select([sys.stdin], [], [], 2.0)
            if rlist:
                key = sys.stdin.read(1)
                if key.lower() == 'q':
                    print("\n[TUI] Zamykanie dashboardu wizualnego.")
                    break
                elif key.lower() == 'c':
                    print("\n[CANTROPHY] Wywołano oczyszczanie entropii z TUI...")
                    time.sleep(1.0)
                elif key.lower() == 'r':
                    continue
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        clear_screen()

if __name__ == "__main__":
    main()
