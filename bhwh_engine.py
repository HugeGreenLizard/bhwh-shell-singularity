#!/usr/bin/env python3
from event_horizon import EventHorizon
from black_hole import BlackHole
from white_hole import WhiteHole

class BHWHEngine:
    def __init__(self):
        print("========================================================")
        print("      BHWH SHELL — PEŁNY CYKL OSOBLIWOŚCI AKTYWNY       ")
        print("========================================================")
        self.horizon = EventHorizon()
        self.singularity = BlackHole()
        self.emitter = WhiteHole()
        print("========================================================\n")

    def execute_stream(self, raw_input: str):
        print(f"[STRUMIEŃ WEJŚCIOWY] '{raw_input}'")
        
        # Obsługa potoków (Wormhole Pipe Chaining / Gravitational Jet Streams) przez znak '|'
        stages = [s.strip() for s in raw_input.split("|")]
        current_input = stages[0]
        latest_atom = None
        
        for idx, stage in enumerate(stages):
            print(f"  [🌀 WORMHOLE STAGE {idx+1}/{len(stages)}] Impuls: '{stage}'")
            
            # 1. Horyzont Zdarzeń (Filtr i normalizacja)
            horizon_result = self.horizon.cross(stage)
            if horizon_result["status"] != "PASSED":
                print(f"  [❌ SINGULARITY REJECT] Odrzucono na Horyzoncie (Stage {idx+1}): {horizon_result['reason']}\n" + "-"*50)
                return False
                
            print(f"  [✔ PASSED] Horyzont miniony. Ładunek: '{horizon_result['payload']}' (Masa: {horizon_result['mass']}b)")
            
            # 2. Czarna Dziura (Akwizycja i kompresja do dysku akrecyjnego)
            bh_result = self.singularity.ingest(horizon_result["payload"])
            print(f"  [🕳 BLACK HOLE] Pochłonięto do dysku akrecyjnego! Podpis: #{bh_result['singularity_signature']}")
            
            # Pobranie najnowszego atomu wiedzy z dysku
            latest_atom = self.singularity.inspect_core()[-1]
            current_input = f"STAGE_{idx+1}_RESULT({horizon_result['payload']}) -> SIG:#{bh_result['singularity_signature']}"
        
        # 3. Biała Dziura (Bezentropijna emisja na zewnątrz po przejściu tunelu)
        exec_res = f"SUCCESS: Potok (Wormhole) pomyślnie zrealizowany w {len(stages)} etapach. Stan końcowy: {current_input}"
        emission_result = self.emitter.emit(latest_atom, execution_result=exec_res)
        print(emission_result)
        print("-" * 50)
        return True

if __name__ == "__main__":
    engine = BHWHEngine()
    
    # Testowy pełny cykl strumieni (w tym potoki / Wormhole Pipe Chaining)
    test_inputs = [
        "sys_core_init --force",
        "load_matrix aeon_mesh_v2 | optimize_tensor --level=5 | emit_omega",
        "   ", # Pusty impuls (zatrzymany na Horyzoncie)
        "@@@###$$$%%%^^^", # Szum (odrzucony)
        "quantum_state_sync --target=E8"
    ]
    
    for cmd in test_inputs:
        engine.execute_stream(cmd)
        
    print(f"\n[STAN KOŃCOWY OSOBLIWOŚCI] Łączna liczba atomów w dysku: {len(engine.singularity.inspect_core())}")
