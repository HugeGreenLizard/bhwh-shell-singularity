#!/usr/bin/env python3
"""
ai_bulk_generator.py — Masowy Generator Prac Naukowych
Przeszukuje katalog preprintów OpenAI_MATH i automatycznie generuje
traktaty naukowe według standardu S-AI-T v1.0.
"""

import os
import sys
from pathlib import Path
from ai_paper_generator import generate_paper

PREPRINTS_DIR = Path.home() / "OpenAI_MATH" / "full_REPO" / "preprints"

def generate_bulk(limit: int = 5):
    if not PREPRINTS_DIR.exists():
        print(f"[X] Brak katalogu: {PREPRINTS_DIR}")
        return
        
    subdirs = [d for d in PREPRINTS_DIR.iterdir() if d.is_dir()]
    print(f"[BULK] Znaleziono {len(subdirs)} katalogów preprintów. Generuję pierwszych {limit}...")
    
    count = 0
    for d in subdirs[:limit]:
        title = d.name.replace("-", " ").replace("September", "").replace("October", "").replace("2026", "").strip()
        print(f"\n[BULK] Generowanie traktatu dla: {title}")
        generate_paper(str(d), title)
        count += 1
        
    print(f"\n[✔ BULK] Pomyślnie wygenerowano {count} nowych traktatów naukowych!")

if __name__ == "__main__":
    limit = int(sys.argv[1]) if len(sys.argv) > 1 else 5
    generate_bulk(limit)
