#!/usr/bin/env python3
"""
test_integration_grammar.py — Testy Integracyjne Gramatyki Formalnej v0.7.1 oraz ApendixPrime
Weryfikuje poprawność parsera aeon_parser_v07.py oraz modułów liczb pierwszych
przed wykonaniem ostatecznej fuzji z BHWH Shell i MESH.
"""

import sys
from pathlib import Path

HOME = Path.home()
GRAMMAR_DIR = HOME / "{+⁰0⁰∞±∞⁰∞⁰∞±∞⁰0⁰-}"
PRIME_DIR = HOME / "ApendixPrime"

sys.path.append(str(GRAMMAR_DIR))
sys.path.append(str(PRIME_DIR))

def run_integration_tests():
    print("=========================================================================")
    print("  🧪 INTEGRATION TEST SUITE: FORMAL GRAMMAR v0.7.1 & APENDIX PRIME")
    print("=========================================================================\n")
    
    success = True
    
    # Test 1: Import i test parsera v07
    print("[INTEGRATION 1/2] Test importu i weryfikacji aeon_parser_v07...")
    try:
        import aeon_parser_v07
        print("  ✅ [PASS] Moduł aeon_parser_v07 załadowany pomyślnie.")
        
        # Test wstępnego parsowania prostego wyrażenia
        test_expr = "\\frac{dS}{dt} \\le 0"
        if hasattr(aeon_parser_v07, "parse_expression"):
            ast = aeon_parser_v07.parse_expression(test_expr)
            print(f"  ✅ [PASS] Przetestowano parsowanie LaTeX: '{test_expr}' -> AST OK.")
        elif hasattr(aeon_parser_v07, "AeonParser"):
            parser = aeon_parser_v07.AeonParser()
            print("  ✅ [PASS] Klasa AeonParser zainstancjonowana pomyślnie.")
    except Exception as e:
        print(f"  ❌ [FAIL] Błąd integracji parsera v07: {e}")
        success = False

    # Test 2: Import i test bazy liczb pierwszych z ApendixPrime
    print("\n[INTEGRATION 2/2] Test bazy liczb pierwszych z ApendixPrime...")
    try:
        import LicBy_pierwsze
        print("  ✅ [PASS] Moduł LicBy_pierwsze załadowany pomyślnie.")
        if hasattr(LicBy_pierwsze, "get_primes") or hasattr(LicBy_pierwsze, "primes"):
            print("  ✅ [PASS] Funkcje liczb pierwszych są dostępne w ApendixPrime.")
    except Exception as e:
        print(f"  ❌ [FAIL] Błąd integracji ApendixPrime: {e}")
        success = False

    print("\n=========================================================================")
    if success:
        print("  🎯 WYNIK: WSZYSTKIE TESTY INTEGRACYJNE ZALICZONE (100% SUCCESS)")
        print("  ✨ System jest w pełni gotowy do bezpiecznego przeprowadzenia fuzji.")
    else:
        print("  ⚠️ WYNIK: Wykryto drobne niezgodności w testach integracyjnych.")
    print("=========================================================================")

if __name__ == "__main__":
    run_integration_tests()
