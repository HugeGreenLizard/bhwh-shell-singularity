#!/usr/bin/env python3
"""
push_to_gh.py — Autonomiczny moduł synchronizacji z GitHubem
Dynamicznie odczytuje token z pliku ~/git_token.md i synchronizuje stan siłowo (force).
"""

import subprocess
from pathlib import Path

SHELL_DIR = Path(__file__).parent.resolve()

def get_token():
    token_file = Path.home() / "git_token.md"
    if not token_file.exists():
        return None
    try:
        content = token_file.read_text(encoding="utf-8")
        for line in content.splitlines():
            for part in line.split():
                clean_part = part.strip("`*#_")
                if clean_part.startswith("ghp_") or clean_part.startswith("github_pat_"):
                    return clean_part
    except Exception:
        pass
    return None

def push():
    print("[PUSH] Inicjalizacja autonomicznego wysyłania do chmury OMEGA...")
    token = get_token()
    
    if not token:
        print("❌ [FAILED] Nie udało się odczytać tokenu z ~/git_token.md.")
        return

    print("[PUSH] ✅ Token odczytany pomyślnie. Synchronizacja z wymuszeniem (force)...")
    repo_url = f"https://{token}@github.com/HugeGreenLizard/bhwh-shell-singularity.git"
    
    # Ustawienie remote URL z tokenem w locie
    subprocess.run(["git", "remote", "set-url", "origin", repo_url], cwd=SHELL_DIR, capture_output=True)
    
    # Push z flagą --force do czystej historii
    p = subprocess.run(["git", "push", "-u", "origin", "master", "--force"], cwd=SHELL_DIR, capture_output=True, text=True)
    
    print("PUSH OUTPUT:\n", p.stdout)
    if p.stderr:
        print("PUSH STDERR:\n", p.stderr)
        
    if p.returncode == 0:
        print("✅ [SUCCESS] Pomyślnie zsynchronizowano czyste repozytorium bhwh-shell-singularity z GitHubem!")
    else:
        print("❌ [FAILED] Błąd podczas pushowania.")

if __name__ == "__main__":
    push()
