#!/usr/bin/env python3
from event_horizon import EventHorizon
import sys

def interactive_test():
    eh = EventHorizon()
    print("\n========================================================")
    print("      BHWH SHELL — INTERAKTYWNY TEST HORYZONTU ZDARZEŃ   ")
    print("========================================================")
    print("Wpisz dowolny ciąg (komendę, tekst lub szum). Wpisz 'EXIT', aby zakończyć.\n")
    
    while True:
        try:
            raw = input("EventHorizon (In) > ")
            if raw.strip().upper() == "EXIT":
                print("\n[HORIZON] Zamykanie bramy horyzontu. System stabilny.")
                break
            
            result = eh.cross(raw)
            
            # Kolorowanie statusu dla przejrzystości w terminalu
            if result["status"] == "PASSED":
                print(f"  [✔ PASSED] Masa: {result['mass']} bajtów | Znormalizowany ładunek: '{result['payload']}'")
            else:
                print(f"  [❌ REJECTED] Powód: {result['reason']}")
            print("-" * 60)
            
        except (KeyboardInterrupt, EOFError):
            print("\n[HORIZON] Przerwano strumień wejściowy.")
            break

if __name__ == "__main__":
    interactive_test()
