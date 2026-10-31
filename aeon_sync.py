#!/usr/bin/env python3
"""
aeon_sync.py — Most GitHub i Sieciowa Synchronizacja dla BHWH Shell
Automatycznie synchronizuje stan osobliwości (singularity_state.json)
oraz artefakty z dedykowanym repozytorium GitHub.
"""

import subprocess
import os
from pathlib import Path

SHELL_DIR = Path(__file__).parent.resolve()

def run_git_command(cmd):
    try:
        result = subprocess.run(
            cmd,
            shell=True,
            cwd=SHELL_DIR,
            capture_output=True,
            text=True,
            timeout=15
        )
        return result.returncode == 0, result.stdout.strip() or result.stderr.strip()
    except Exception as e:
        return False, str(e)

def sync_to_github():
    print("[AEON-SYNC] Rozpoczynam synchronizację stanu BHWH Shell z GitHubem...")
    
    # 1. Sprawdzenie czy git jest zainicjalizowany
    if not (SHELL_DIR / ".git").exists():
        print("[AEON-SYNC] Inicjalizacja lokalnego repozytorium Git...")
        success, out = run_git_command("git init")
        if not success:
            print(f"[❌ ERROR] Nie udało się zainicjalizować git: {out}")
            return False

    # 2. Dodanie plików projektu
    success, out = run_git_command("git add .")
    if not success:
        print(f"[❌ WARNING] Ostrzeżenie przy add: {out}")

    # 3. Sprawdzenie statusu
    success, out = run_git_command("git status --porcelain")
    if not out:
        print("[AEON-SYNC] Brak nowych zmian do zsynchronizowania. Dysk akrecyjny jest aktualny.")
        return True

    # 4. Commit
    commit_msg = "Ω-SYNC: Automatyczna synchronizacja dysku akrecyjnego i stanu MESH [OMEGA-ETERNAL]"
    success, out = run_git_command(f'git commit -m "{commit_msg}"')
    if not success and "nothing to commit" not in out:
        print(f"[❌ ERROR] Błąd podczas commitu: {out}")
        return False
    print(f"[AEON-SYNC] ✅ Utworzono commit synchronizacyjny.")

    # 5. Push do remote
    success, out = run_git_command("git push origin main")
    if not success:
        success, out = run_git_command("git push origin master")
        if not success:
            print(f"[⚠️ NOTICE] Zmiany zatwierdzone lokalnie. Konfiguruję zdalne repozytorium...")
            return False

    print("[⚪ AEON-SYNC] ✅ Pomyślnie zsynchronizowano stan osobliwości z chmurą GitHub!")
    return True

if __name__ == "__main__":
    sync_to_github()
