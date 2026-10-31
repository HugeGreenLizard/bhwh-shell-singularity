import re

class EventHorizon:
    def __init__(self):
        print("[HORIZON] Inicjalizacja Horyzontu Zdarzeń (Event Horizon)... OK")
        print("[HORIZON] Grawitacyjna sieć filtrująca i normalizator aktywny.")

    def cross(self, raw_input: str) -> dict:
        """
        Przekraczanie horyzontu zdarzeń przez surową komendę/dane.
        Wykonuje walidację, filtrację entropii i normalizację.
        """
        if not raw_input or not raw_input.strip():
            return {"status": "REJECTED", "reason": "Zero-mass input (pusty sygnał)"}

        cleaned = raw_input.strip()
        
        # Filtr antyentropijny (prosty test szumu)
        if len(re.findall(r"[^\w\s\-\.\/\:]", cleaned)) > len(cleaned) * 0.4:
            return {"status": "SINGULARITY_REJECT", "reason": "Wysoka entropia wejściowa (szum astrofizyczny)"}

        # Normalizator grawitacyjny (wstępna unifikacja składni)
        normalized = re.sub(r"\s+", " ", cleaned)
        
        return {
            "status": "PASSED",
            "mass": len(normalized),
            "payload": normalized
        }
