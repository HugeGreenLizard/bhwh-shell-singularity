import time

class WhiteHole:
    def __init__(self):
        print("[WHITE_HOLE] Inicjalizacja Białej Dziury (White Hole)... OK")
        print("[WHITE_HOLE] Bezentropijna emisja wyników wykonania aktywna.")

    def emit(self, knowledge_atom: dict, execution_result: str) -> str:
        """
        Bezentropijna emisja (delta S <= 0) wyników wykonania komendy z dysku akrecyjnego.
        """
        payload = knowledge_atom.get("payload", "")
        sig = knowledge_atom.get("signature", "0000000000")
        
        output = f"\n[⚪ WHITE_HOLE EMISSION] >>> [Osobliwość #{sig}]\n"
        output += f"  Komenda źródłowa   : {payload}\n"
        output += f"  Wynik wykonania    :\n"
        # Wcięcie dla czytelności wynikowego stdout
        for line in execution_result.splitlines():
            output += f"    │ {line}\n"
        output += f"  Entropia Systemowa : ΔS <= 0 (Czysta Emisja)\n"
        return output
