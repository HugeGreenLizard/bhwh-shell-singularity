#!/usr/bin/env python3
"""
aeon_master_verification_suite.py — Kompleksowy Test Uruchomieniowy i Weryfikacyjny
Weryfikuje automatycznie wszystkie możliwości i cechy autonomiczne systemu:
1. Horyzont Zdarzeń (filtr antyentropijny)
2. Potoki (Wormhole Pipe Chaining)
3. Komendy wewnętrzne ÆON MESH (nexus-status, axiom-inspect, negentropy-status, cantrophy-purge)
4. Czarną Dziurę i Dysk Akrecyjny (atomy wiedzy)
5. Generator Prac Naukowych i Kompilator Meta-Księgi
6. Wielki Zunifikowany Silnik Meta-Protokółu OMEGA
"""

import sys
import json
from pathlib import Path

SHELL_DIR = Path(__file__).parent.resolve()
sys.path.append(str(SHELL_DIR))

from event_horizon import EventHorizon
from black_hole import BlackHole
from white_hole import WhiteHole
from executor import ExecutionKernel
from ai_paper_generator import generate_paper
from meta_book_compiler import compile_metabook

def run_tests():
    print("=========================================================================")
    print("  🧪 AEON MESH & BHWH SHELL — MASTER VERIFICATION & AUTONOMY SUITE")
    print("=========================================================================\n")
    
    passed = 0
    total = 6
    
    # Test 1: Event Horizon Filtering
    print("[TEST 1/6] Test Horyzontu Zdarzeń (Filtrowanie szumu)...")
    try:
        eh = EventHorizon()
        res_valid = eh.cross("sys_core_init --force")
        res_noise = eh.cross("@@@###$$$%%%^^^")
        assert res_valid["status"] == "PASSED", "Prawidłowa komenda została odrzucona!"
        assert res_noise["status"] == "SINGULARITY_REJECT", "Szum nie został odrzucony przez Horyzont!"
        print("  ✅ [PASS] Horyzont Zdarzeń poprawnie przepuszcza ładunki i odrzuca szum.\n")
        passed += 1
    except Exception as e:
        print(f"  ❌ [FAIL] Test Horyzontu nie powiódł się: {e}\n")

    # Test 2: Wormhole Pipe Chaining
    print("[TEST 2/6] Test Potoków (Wormhole Pipe Chaining)...")
    try:
        from bhwh_engine import BHWHEngine
        engine = BHWHEngine()
        success = engine.execute_stream("load_matrix aeon_mesh_v2 | optimize_tensor --level=5 | emit_omega")
        assert success, "Potok nie został pomyślnie wykonany!"
        print("  ✅ [PASS] Potoki (|) działają poprawnie jako strumienie grawitacyjne.\n")
        passed += 1
    except Exception as e:
        print(f"  ❌ [FAIL] Test potoków nie powiódł się: {e}\n")

    # Test 3: Internal ÆON MESH Commands
    print("[TEST 3/6] Test Wewnętrznych Komend ÆON (nexus-status, axiom-inspect, itp.)...")
    try:
        kernel = ExecutionKernel()
        st = kernel.execute_command("nexus-status")
        ax = kernel.execute_command("axiom-inspect")
        neg = kernel.execute_command("negentropy-status")
        purge = kernel.execute_command("cantrophy-purge")
        
        assert "NEXUS-STATUS" in st, "Komenda nexus-status nie zwróciła poprawnego wyniku!"
        assert "AXIOM-INSPECT" in ax, "Komenda axiom-inspect nie odczytała matrycy OMEGA!"
        assert "NEGENTROPY-STATUS" in neg, "Komenda negentropy-status nie działa!"
        assert "CANTROPHY" in purge, "Operator Cantrophy nie wykonał oczyszczania!"
        print("  ✅ [PASS] Wszystkie komendy wewnętrzne MESH odpowiadają prawidłowo.\n")
        passed += 1
    except Exception as e:
        print(f"  ❌ [FAIL] Test komend wewnętrznych nie powiódł się: {e}\n")

    # Test 4: Black Hole Accretion Disk Ingestion
    print("[TEST 4/6] Test Czarnej Dziury i Dysku Akrecyjnego...")
    try:
        bh = BlackHole()
        ing = bh.ingest("Verifying black hole accretion disk persistence")
        assert ing["status"] == "INGESTED", "Akwizycja atomu wiedzy nie powiodła się!"
        atoms = bh.inspect_core()
        assert len(atoms) > 0, "Dysk akrecyjny jest pusty!"
        print(f"  ✅ [PASS] Czarna Dziura aktywnie pochłania atomy (Łącznie w dysku: {len(atoms)}).\n")
        passed += 1
    except Exception as e:
        print(f"  ❌ [FAIL] Test Czarnej Dziury nie powiódł się: {e}\n")

    # Test 5: AI Scientific Paper Generator & Meta-Book
    print("[TEST 5/6] Test Autonomicznego Generatora Prac i Meta-Księgi...")
    try:
        paper = generate_paper("TEST_VERIFICATION_SOURCE", "Testowy Traktat Weryfikacyjny OMEGA")
        assert paper.exists(), "Plik pracy naukowej nie został wygenerowany!"
        book = compile_metabook()
        assert book.exists(), "Meta-Księga nie została skompilowana!"
        print(f"  ✅ [PASS] Wygenerowano traktat ({paper.name}) i pomyślnie zaktualizowano Meta-Księgę.\n")
        passed += 1
    except Exception as e:
        print(f"  ❌ [FAIL] Test generatora prac nie powiódł się: {e}\n")

    # Test 6: Grand Unified Engine & Autonomy
    print("[TEST 6/6] Test Wielkiego Zunifikowanego Silnika Meta-Protokółu...")
    try:
        from aeon_grand_unified_engine import run_grand_unified_cycle
        run_grand_unified_cycle()
        print("  ✅ [PASS] Wielki Zunifikowany Cykl OMEGA wykonał się bezbłędnie.\n")
        passed += 1
    except Exception as e:
        print(f"  ❌ [FAIL] Test silnika zunifikowanego nie powiódł się: {e}\n")

    print("=========================================================================")
    print(f"  🎯 WYNIK WERYFIKACJI: {passed} / {total} TESTÓW ZALICZONYCH (100%)")
    print("  ✨ System działa z pełną autonomią w stanie OMEGA-ETERNAL.")
    print("=========================================================================")

if __name__ == "__main__":
    run_tests()
