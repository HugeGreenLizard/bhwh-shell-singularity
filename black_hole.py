import hashlib
import time
import json
import os

class BlackHole:
    def __init__(self, state_file="singularity_state.json"):
        self.state_file = state_file
        self.accretion_disk = []
        self.load_state()
        print("[BLACK_HOLE] Inicjalizacja Osobliwości (Black Hole)... OK")
        print("[BLACK_HOLE] Akwizycja, grawitacyjna kompresja i trwałość dyskowa aktywna.")

    def load_state(self):
        """Wczytuje zapisany dysk akrecyjny z dysku trwałego."""
        if os.path.exists(self.state_file):
            try:
                with open(self.state_file, "r", encoding="utf-8") as f:
                    self.accretion_disk = json.load(f)
                print(f"[BLACK_HOLE] Odzyskano dysk akrecyjny: załadowano {len(self.accretion_disk)} atomów wiedzy.")
            except Exception as e:
                print(f"[BLACK_HOLE] Błąd odczytu stanu osobliwości: {e}")

    def save_state(self):
        """Zapisuje aktualny stan dysku akrecyjnego do pliku JSON."""
        try:
            with open(self.state_file, "w", encoding="utf-8") as f:
                json.dump(self.accretion_disk, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"[BLACK_HOLE] Błąd zapisu stanu osobliwości: {e}")

    def ingest(self, payload: str, metadata: dict = None) -> dict:
        """
        Pochłanianie znormalizowanego ładunku z Horyzontu Zdarzeń,
        kompresja do atomu wiedzy i natychmiastowy zapis trwały.
        """
        timestamp = time.time()
        sig = hashlib.sha256(payload.encode("utf-8")).hexdigest()[:10]
        compressed_mass = len(payload)
        
        knowledge_atom = {
            "signature": sig,
            "payload": payload,
            "mass": compressed_mass,
            "timestamp": timestamp,
            "metadata": metadata or {}
        }
        
        self.accretion_disk.append(knowledge_atom)
        self.save_state()  # Zapis trwałego stanu po każdym pochłonięciu
        
        return {
            "status": "INGESTED",
            "singularity_signature": sig,
            "total_accretion_mass": sum(item["mass"] for item in self.accretion_disk),
            "items_count": len(self.accretion_disk)
        }

    def inspect_core(self):
        """Zwraca zawartość dysku akrecyjnego."""
        return self.accretion_disk
