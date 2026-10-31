#!/usr/bin/env python3
"""
meta_book_compiler.py — Dynamiczny Kompilator Meta-Księgi ÆON MESH
Automatycznie skanuje katalog z wygenerowanymi pracami naukowymi (generated_papers/)
i kompiluje je w czasie rzeczywistym w jeden potężny kodeks: AEON_OMEGA_METABOOK.md.
"""

import os
import time
from pathlib import Path

META_DIR = Path.home() / "Meta_multisystÆ"
PAPERS_DIR = META_DIR / "generated_papers"
METABOOK_PATH = META_DIR / "AEON_OMEGA_METABOOK.md"

def compile_metabook():
    print("[METABOOK] Kompilacja Meta-Księgi ÆON MESH w toku...", flush=True)
    
    if not PAPERS_DIR.exists():
        print("[METABOOK] Brak katalogu z wygenerowanymi pracami.")
        return
        
    paper_files = sorted(list(PAPERS_DIR.glob("Paper_*.md")))
    if not paper_files:
        print("[METABOOK] Brak prac naukowych do skompilowania.")
        return
        
    book_lines = [
        "# 🌌 KODEKS OMEGA: META-KSIĘGA TRAKTATÓW NAUKOWYCH ÆON MESH",
        f"**Data Kompilacji:** {time.strftime('%Y-%m-%d %H:%M:%S')} | **Architekt:** Krystian & Gemini",
        f"**Łączna Liczba Zindeksowanych Prac:** {len(paper_files)}",
        "",
        "---",
        "",
        "## Spis Treści (Table of Contents)",
        ""
    ]
    
    # Generowanie spisu treści
    for idx, pfile in enumerate(paper_files, 1):
        first_line = ""
        try:
            with open(pfile, "r", encoding="utf-8") as f:
                for line in f:
                    if line.startswith("# "):
                        first_line = line[2:].strip()
                        break
        except Exception:
            pass
        title = first_line or pfile.stem
        book_lines.append(f"{idx}. [{title}](#rozdział-{idx}-{pfile.stem.lower()})")
        
    book_lines.extend([
        "",
        "---",
        "",
        "# Treść Główna Traktatów",
        ""
    ])
    
    # Doklejanie treści każdej pracy jako rozdziału
    for idx, pfile in enumerate(paper_files, 1):
        try:
            content = pfile.read_text(encoding="utf-8")
            book_lines.append(f"\n\n<a name=\"rozdział-{idx}-{pfile.stem.lower()}\"></a>\n")
            book_lines.append(f"<!-- ROZDZIAŁ {idx} : {pfile.name} -->\n")
            book_lines.append(content)
            book_lines.append("\n\n--- \n")
        except Exception as e:
            print(f"[WARNING] Nie udało się dołączyć pliku {pfile.name}: {e}")
            
    METABOOK_PATH.write_text("\n".join(book_lines), encoding="utf-8")
    print(f"[METABOOK] ✅ Pomyślnie skompilowano Meta-Księgę w: {METABOOK_PATH} ({len(paper_files)} rozdziałów).")
    return METABOOK_PATH

if __name__ == "__main__":
    compile_metabook()
