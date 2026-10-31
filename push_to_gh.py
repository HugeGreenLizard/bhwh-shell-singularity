#!/usr/bin/env python3
"""
push_to_gh.py — Autonomiczny moduł synchronizacji z GitHubem
Dynamicznie odczytuje token z pliku ~/git_token.md.
"""

import subprocess
from pathlib import Path

SHELL_DIR = Path(__file__).parent.resolve()

def get_token():
    token_file = Path.home() / "git_token.md"
    if not token_file.exists():
        print(f"[DEBUG] Brak pliku: {token_file}")
        return None
        
    try:
        content = token_file.read_text(encoding="utf-8")
        lines = content.splitlines()
        
        # Przeszukiwanie linii w poszukiwaniu ghp_ lub github_pat_
        for i, line in enumerate(lines):
            # Sprawdzenie słów w bieżącej linii
            for part in line.split():
                if part.startswith("ghp_") or part.startswith("github_pat_"):
                    return part.strip()
            # Sprawdzenie czy token jest w następnej linii (częste po nagłówku)
            if "token" in line.lower() and i + 1 < len(lines):
                next_val = lines[i + 1].strip()
                if next_val.startswith("ghp_") or next_val.startswith("github_pat_"):
                    return next_val
                    
        # Awaryjne przeszukiwanie całego pliku słowo po słowie
        for line in lines:
            for part in line.split():
                clean_part = part.strip("`*#_")
                if clean_part.startswith("ghp_") or clean_part.startswith("github_pat_"):
                    return clean_part
                    
    except Exception as e:
        print(f"[ERROR] Błąd parsowania pliku tokenu: {e}")
        
    return None

def push():
    print("[PUSH] Inicjalizacja autonomicznego wysyłania do chmury OMEGA...")
    token = get_token()
    
    if not token:
        print("❌ [FAILED] Nie udało się odczytać tokenu z ~/git_token.md.")
        return

    print("[PUSH] ✅ Token odczytany pomyślnie z pliku lokalnego.")
    repo_url = f"https://{token}@github.com/HugeGreenLizard/bhwh-shell-singularity.git"
    
    # Ustawienie remote URL z tokenem w locie
    subprocess.run(["git", "remote", "set-url", "origin", repo_url], cwd=SHELL_DIR, capture_output=True)
    
    # Push do repozytorium
    p = subprocess.run(["git", "push", "-u", "origin", "master"], cwd=SHELL_DIR, capture_output=True, text=True)
    
    print("PUSH OUTPUT:\n", p.stdout)
    if p.stderr:
        print("PUSH STDERR:\n", p.stderr)
        
    if p.returncode == 0:
        print("✅ [SUCCESS] Pomyślnie wypchnięto repozytorium bhwh-shell-singularity na GitHub!")
    else:
        print("❌ [FAILED] Błąd podczas pushowania.")

if __name__ == "__main__":
    push()
