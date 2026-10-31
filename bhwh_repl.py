#!/usr/bin/env python3
from event_horizon import EventHorizon
from black_hole import BlackHole
from white_hole import WhiteHole
from executor import ExecutionKernel
import sys

def main():
    print("========================================================")
    print("      BHWH SHELL — EXECUTING SINGULARITY REPL           ")
    print("      Architekt: Krystian | Status: OMEGA-ETERNAL       ")
    print("========================================================")
    
    horizon = EventHorizon()
    singularity = BlackHole()
    emitter = WhiteHole()
    kernel = ExecutionKernel()
    
    print("\n[SYSTEM] Powłoka wykonawcza gotowa. Wpisz komendę systemową, 'STATUS' lub 'EXIT'.\n")
    
    while True:
        try:
            raw_input_str = input("{BHWH-Shell} > ")
            if not raw_input_str:
                continue
            
            cmd = raw_input_str.strip()
            
            if cmd.upper() in ["EXIT", "QUIT"]:
                print("\n[SYSTEM] Zamykanie osobliwości. Dysk akrecyjny zachowany w stabilnym stanie.")
                break
                
            if cmd.upper() == "STATUS":
                atoms = singularity.inspect_core()
                print(f"\n[STAN OSOBLIWOŚCI] Łączna liczba atomów w dysku: {len(atoms)}")
                for atom in atoms:
                    print(f" - #{atom['signature']} : {atom['payload']} ({atom['mass']} bajtów)")
                print("-" * 50)
                continue
            
            # 1. Horyzont Zdarzeń (Filtr i normalizacja)
            horizon_result = horizon.cross(cmd)
            if horizon_result["status"] != "PASSED":
                print(f"  [❌ SINGULARITY REJECT] Odrzucono na Horyzoncie: {horizon_result['reason']}\n" + "-"*50)
                continue
                
            # 2. Czarna Dziura (Akwizycja, kompresja i zapis trwałego atomu wiedzy)
            bh_result = singularity.ingest(horizon_result["payload"])
            latest_atom = singularity.inspect_core()[-1]
            
            # 3. Kernel Wykonawczy (Realne wykonanie w systemie operacyjnym)
            exec_output = kernel.execute_command(latest_atom["payload"])
            
            # 4. Biała Dziura (Bezentropijna emisja wyniku systemowego)
            emission = emitter.emit(latest_atom, exec_output)
            print(emission)
            print("-" * 50)
            
        except (KeyboardInterrupt, EOFError):
            print("\n[SYSTEM] Przerwano strumień powłoki.")
            break

if __name__ == "__main__":
    main()
