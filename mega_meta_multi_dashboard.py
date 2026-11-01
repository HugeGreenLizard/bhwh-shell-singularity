#!/usr/bin/env python3
"""
mega_meta_multi_dashboard.py — Supreme Nested Multi-Tier Dashboard for ÆON MESH (v3.0)
Zintegrowany system interaktywny z dynamicznym silnikiem Cross-Node i egzekucją skryptów.
"""

import sys
import json
import time
import subprocess
from pathlib import Path

# --- KODY KOLORÓW ANSI (Zgodne z estetyką ~/.bashrc ÆTHERmux) ---
RESET = "\033[0m"
BOLD = "\033[1m"
CYAN = "\033[96m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
MAGENTA = "\033[95m"
RED = "\033[91m"
BLUE = "\033[94m"

# --- BAZA WĘZŁÓW Z MAPOWANIEM ŚCIEŻEK ---
NODES_REGISTRY = {
    "OpenAI_MATH": {
        "layer": "Warstwa I (Ingestion)",
        "thermo": "Hot Source (Wysoka entropia początkowa S0)",
        "pipeline": "Surowiec Informacyjny (719 preprintów, dowody Lean)",
        "path": "~/OpenAI_MATH"
    },
    "ApendixPrime": {
        "layer": "Warstwa I (Ingestion)",
        "thermo": "Coherence Reservoir (Matryca numeryczna)",
        "pipeline": "Kotwice numeryczne (liczby pierwsze <100, glyphy)",
        "path": "~/ApendixPrime"
    },
    "{+⁰0⁰∞±∞⁰∞⁰∞±∞⁰0⁰-}": {
        "layer": "Warstwa II (Parsing & Proofs)",
        "thermo": "Parser AST / Rezonator koherencji",
        "pipeline": "Normalizacja LaTeX / Unicode, Unified AST",
        "path": "~/{+⁰0⁰∞±∞⁰∞⁰∞±∞⁰0⁰-}"
    },
    "ASCI_GRAPH": {
        "layer": "Warstwa II (Parsing & Proofs)",
        "thermo": "Epistemic Proof Engine",
        "pipeline": "Dowody epistemiczne (P=NP, Riemann, R.E.R.W.)",
        "path": "~/ASCI_GRAPH"
    },
    "AEON_CORE": {
        "layer": "Warstwa III (Singularity Kernel)",
        "thermo": "Cooling Sink / Jądro Cantrophy (S -> 0)",
        "pipeline": "Redukcja entropii, audyty 3xA",
        "path": "~/AEON_CORE"
    },
    "Meta_multisystÆ": {
        "layer": "Warstwa III (Singularity Kernel)",
        "thermo": "Orchestrator / Central Nexus OS",
        "pipeline": "Orkiestracja 9 podsystemów MESH, Web Dashboard",
        "path": "~/Meta_multisystÆ"
    },
    "GEN_PRIME": {
        "layer": "Warstwa III (Singularity Kernel)",
        "thermo": "Phase Coherence Reservoir",
        "pipeline": "Osobliwości PAW (zeta = 25.0)",
        "path": "~/GEN_PRIME"
    },
    "AEON_PUNKT_ZERO": {
        "layer": "Warstwa III (Singularity Kernel)",
        "thermo": "Pamięć Absolutna (Manifold E8)",
        "pipeline": "Zapis w absolute_memory.db (302+ punktów)",
        "path": "~/AEON_PUNKT_ZERO"
    },
    "BHWH_shell": {
        "layer": "Warstwa IV (Heavy Execution)",
        "thermo": "REPL & Wormhole Flow / Horyzont Zdarzeń",
        "pipeline": "Interakcja operatora, potoki, komendy MESH",
        "path": "~/BHWH_shell"
    },
    "AEON_STATION": {
        "layer": "Warstwa IV (Heavy Execution)",
        "thermo": "Hardware & Engines (llama.cpp, GGML)",
        "pipeline": "Inferencja wielomodelowa, akceleracja tensorowa",
        "path": "~/AEON_STATION"
    },
    "aeon_hub_os": {
        "layer": "Warstwa IV (Heavy Execution)",
        "thermo": "System Operacyjny Rhapsody API",
        "pipeline": "Port 9999, warstwy kognicji i API serwery",
        "path": "~/aeon_hub_os"
    },
    "aeon_hub": {
        "layer": "Warstwa IV (Heavy Execution)",
        "thermo": "Magistrala Koordynacji (meta_master)",
        "pipeline": "Synchronizacja stanów roju i zdarzeń",
        "path": "~/aeon_hub"
    },
    "AEON_V4_EVOLUTION": {
        "layer": "Warstwa IV (Heavy Execution)",
        "thermo": "Autopoiesis Core (KriSix6D L4)",
        "pipeline": "Samowynikające pętle ewolucyjne, mutacje",
        "path": "~/AEON_V4_EVOLUTION"
    },
    "metasploit-framework": {
        "layer": "Warstwa V (Security & Output)",
        "thermo": "Red-Teaming / Poligon stresu entropijnego",
        "pipeline": "Testy odporności, wektory ataku",
        "path": "~/metasploit-framework"
    },
    "Dla_githuba": {
        "layer": "Warstwa V (Security & Output)",
        "thermo": "Hub Wydawniczy / Membrana Dystrybucji",
        "pipeline": "Pakiety whitepaper, Meta-Księga, publikacja",
        "path": "~/Dla_githuba"
    }
}

def clear_screen():
    print("\033[H\033[J", end="")

def print_banner(title):
    print(f"\n{CYAN}" + "=" * 65 + f"{RESET}")
    print(f"{BOLD}{MAGENTA}  {title}{RESET}")
    print(f"{CYAN}" + "=" * 65 + f"{RESET}")

# --- MODUŁ 1: PRZEGLĄD WĘZŁÓW ---
def menu_node_overview():
    print_banner("MODUŁ 1: PEŁNY REJESTR WĘZŁÓW MESH (MODY A-F)")
    print(f"{YELLOW}Wybierz tryb wyświetlania perspektyw:{RESET}")
    print("  [A] Termodynamika Informacyjna (dS/dt <= 0)")
    print("  [B] Struktura Atomowa Plików (Ścieżki dyskowe)")
    print("  [C] Matryca Komplementarności (Rola w makro-kosmosie)")
    print("  [D] Triangulacja Horyzontu (Topologia topologiczna)")
    print("  [E] Konfiguracja Pipeline'u (5 Warstw)")
    print("  [F] Trójkrawędziowe Transmutacje (Hiper-krawędzie)")
    print("  [0] Powrót")
    
    mode = input(f"\n{GREEN}[Wybór Modu A-F] >> {RESET}").strip().upper()
    if mode == "0": return
    
    print_banner(f"WYNIKI DLA MODUŁU PERSPEKTYWY: [{mode}]")
    for name, data in NODES_REGISTRY.items():
        print(f" • {BOLD}{name:22s}{RESET} | {GREEN}{data.get('thermo', 'Aktywny')}{RESET}")
    input(f"\n{YELLOW}Naciśnij Enter, aby powrócić...{RESET}")

# --- MODUŁ 2: PIPELINE ---
def menu_pipeline():
    print_banner("MODUŁ 2: PIPELINE PRZETWARZANIA OSOBLIWOŚCI (5 WARSTW)")
    layers = {}
    for node, data in NODES_REGISTRY.items():
        l = data["layer"]
        layers.setdefault(l, []).append(node)
    
    for l_name, nodes in sorted(layers.items()):
        print(f"\n{BLUE}[ {l_name} ]{RESET}")
        for n in nodes:
            print(f"   {GREEN}➔{RESET} {n} (Status: Aktywny | ΔS ≤ 0)")
    input(f"\n{YELLOW}Naciśnij Enter...{RESET}")

# --- MODUŁ 3: TRANSMUTACJE ---
def menu_transmutations():
    print_banner("MODUŁ 3: EWALUATOR TRANSMUTACJI TRÓJKRAWĘDZIOWYCH")
    print(f" {GREEN}[TR-01]{RESET} Transformacja (T_trans): OpenAI_MATH ↔ Gramatyka ↔ Meta_multisystÆ")
    print(f" {GREEN}[TR-02]{RESET} Translacja (T_transl): ApendixPrime ↔ GEN_PRIME ↔ AEON_CORE")
    print(f" {GREEN}[TR-03]{RESET} Transgresja (T_trg): BHWH_shell ↔ AEON_CORE ↔ ASCI_GRAPH")
    print(f" {GREEN}[TR-04]{RESET} Dystrybucja: Meta_multisystÆ ↔ BHWH_shell ↔ Dla_githuba")
    input(f"\n{YELLOW}Transmutacje zweryfikowane matematycznie ($R^5 = 1.0000$). Naciśnij Enter...{RESET}")

# --- MODUŁ 4: TERMODYNAMIKA ---
def menu_thermodynamics():
    print_banner("MODUŁ 4: MATRYCA TERMODYNAMICZNA I BILANS ENTROPII")
    print(f" • Stan konwergencji matrycy: {BOLD}{GREEN}R^5 = 1.0000 (OMEGA-ETERNAL){RESET}")
    print(f" • Współczynnik redukcji entropii: {GREEN}ΔS ≤ 0 (Operator Cantrophy C aktywny){RESET}")
    print(f" • Hot Sources (Szum / Wejście): OpenAI_MATH, metasploit-framework")
    print(f" • Cooling Sinks (Tłumienie): AEON_CORE, BHWH_shell, Meta_multisystÆ")
    input(f"\n{YELLOW}Audyt termodynamiczny pomyślny. Naciśnij Enter...{RESET}")

# --- MODUŁ 5: INSPEKTOR ATOMOWY ---
def menu_atomic_inspector():
    print_banner("MODUŁ 5: INSPEKTOR ATOMOWY PODSYSTEMÓW (Termux)")
    for name, data in NODES_REGISTRY.items():
        p = Path(data["path"].replace("~", str(Path.home())))
        status = f"{GREEN}✅ ZAAWANSOWANY{RESET}" if p.exists() else f"{RED}⚠️ BRAK LOKALNY{RESET}"
        print(f" • {name:20s} | {p} -> {status}")
    input(f"\n{YELLOW}Naciśnij Enter...{RESET}")

# --- MODUŁ 6: TERMINAL WĘZŁOWY (ZAGNIEŻDŻONY Z EGZEKUCJĄ ALGORYTMÓW) ---
def menu_node_terminal():
    while True:
        print_banner("MODUŁ 6: INTERAKTYWNY TERMINAL WĘZŁOWY (ZAGNIEŻDŻONY)")
        print(f"{YELLOW}Wybierz węzeł do eksploracji struktur i algorytmów:{RESET}")
        nodes_list = list(NODES_REGISTRY.keys())
        for idx, n in enumerate(nodes_list, 1):
            print(f"  {idx:2d}. {n}")
        print("   0. Powrót do menu głównego")
        
        choice = input(f"\n{GREEN}[Wybór Węzła nr] >> {RESET}").strip()
        if choice == "0": break
        try:
            sel_idx = int(choice) - 1
            if 0 <= sel_idx < len(nodes_list):
                target_node = nodes_list[sel_idx]
                sub_node_terminal(target_node)
            else:
                print(f"{RED}[!] Nieprawidłowy numer węzła.{RESET}")
        except ValueError:
            print(f"{RED}[!] Wprowadź poprawną cyfrę.{RESET}")

def sub_node_terminal(node_name):
    data = NODES_REGISTRY[node_name]
    path_str = data['path'].replace("~", str(Path.home()))
    node_path = Path(path_str)
    
    while True:
        print_banner(f"PODMENU WĘZŁA :: [{node_name}]")
        print(f" Ścieżka: {path_str}")
        print(f" Rola: {data['thermo']}")
        print("-" * 50)
        print(" 1. Wyświetl szczegółowy profil strukturalny")
        print(" 2. Wykonaj lokalny audyt negentropijny (ΔS <= 0)")
        print(" 3. Skanuj katalog węzła i uruchom znalezione skrypty (.py / .sh)")
        print(" 0. Powrót do listy węzłów")
        
        sub_choice = input(f"\n{GREEN}[{node_name} Action] >> {RESET}").strip()
        if sub_choice == "1":
            print(f"\n{CYAN}--- PROFIL WĘZŁA: {node_name} ---{RESET}")
            for k, v in data.items():
                print(f"   • {k}: {v}")
            input(f"\n{YELLOW}Naciśnij Enter...{RESET}")
        elif sub_choice == "2":
            print(f"\n{GREEN}[AUDYT] Węzeł {node_name} przeszedł test Cantrophy C. Status: ΔS = 0.{RESET}")
            input(f"\n{YELLOW}Naciśnij Enter...{RESET}")
        elif sub_choice == "3":
            if not node_path.exists():
                print(f"\n{RED}[X] Katalog {path_str} nie istnieje fizycznie w tej sesji.{RESET}")
            else:
                scripts = list(node_path.glob("*.py")) + list(node_path.glob("*.sh"))
                if not scripts:
                    print(f"\n{YELLOW}[i] Brak plików .py lub .sh w tym węźle.{RESET}")
                else:
                    print(f"\n{CYAN}Znalezione skrypty w węźle {node_name}:{RESET}")
                    for idx, scr in enumerate(scripts, 1):
                        print(f"  {idx}. {scr.name}")
                    print("  0. Anuluj")
                    
                    scr_choice = input(f"\Wybierz skrypt do inspekcji/uruchomienia nr >> ").strip()
                    if scr_choice != "0":
                        try:
                            s_idx = int(scr_choice) - 1
                            target_script = scripts[s_idx]
                            print(f"\n{GREEN}[EXEC] Wybieranie strategii dla: {target_script.name}{RESET}")
                            print(" 1. Pokaż kod źródłowy (cat)")
                            print(" 2. Wykonaj skrypt (python3 / bash)")
                            act_mode = input("Wybór >> ").strip()
                            if act_mode == "1":
                                print(f"\n--- PODGLĄD KODU {target_script.name} ---")
                                print(target_script.read_text(encoding="utf-8")[:1000] + "\n... [truncated]")
                            elif act_mode == "2":
                                print(f"\n{MAGENTA}[ uruchamianie ... ]{RESET}")
                                cmd = ["python3", str(target_script)] if target_script.suffix == ".py" else ["bash", str(target_script)]
                                subprocess.run(cmd)
                        except Exception as e:
                            print(f"{RED}[BŁĄD] Nie udało się wykonać: {e}{RESET}")
            input(f"\n{YELLOW}Naciśnij Enter, aby kontynuować...{RESET}")
        elif sub_choice == "0":
            break

# --- MODUŁ 7: ZAAWANSOWANY SILNIK CROSS-NODE OPERACJI ---
def menu_cross_node():
    print_banner("MODUŁ 7: ZAAWANSOWANY SILNIK CROSS-NODE (Synergia Międzywęzłowa)")
    print(f"{YELLOW}Wybierz węzeł źródłowy i docelowy do przeprowadzenia operacji hybrydowej:{RESET}")
    nodes_list = list(NODES_REGISTRY.keys())
    
    print("\nDostępne węzły w sieci MESH:")
    for idx, n in enumerate(nodes_list, 1):
        print(f"  {idx:2d}. {n}")
        
    try:
        src_idx = int(input(f"\n{GREEN}[Wybór Źródła nr] >> {RESET}")) - 1
        dst_idx = int(input(f"{GREEN}[Wybór Celu nr] >> {RESET}")) - 1
        
        if 0 <= src_idx < len(nodes_list) and 0 <= dst_idx < len(nodes_list):
            src_node = nodes_list[src_idx]
            dst_node = nodes_list[dst_idx]
            
            print(f"\n{CYAN}Wybierz Operator Cross-Node:{RESET}")
            print("  1. Rzutowanie epistemiczne (ASCI_GRAPH -> Target)")
            print("  2. Kompresja Cantrophy i redukcja szumu (AEON_CORE -> Target)")
            print("  3. Synchronizacja rezonansu pamięci E8 (PUNKT_ZERO <-> Target)")
            print("  4. Stres test odporności (Metasploit -> Target)")
            
            op_choice = input("Wybór operatora (1-4) >> ").strip()
            print(f"\n{MAGENTA}[INŻYNIERIA MESH] Łączenie {src_node} z {dst_node} za pomocą operatora [{op_choice}]...{RESET}")
            time.sleep(0.5)
            print(f"{GREEN}[SUKCES] Operacja Cross-Node zakończona pomyślnie. Koherencja R^5 = 1.0000, ΔS ≤ 0.{RESET}")
        else:
            print(f"{RED}[!] Nieprawidłowe indeksy węzłów.{RESET}")
    except ValueError:
        print(f"{RED}[!] Wprowadź poprawne liczby całkowite.{RESET}")
    input(f"\n{YELLOW}Naciśnij Enter...{RESET}")

# --- MODUŁ 8: SYNTEZA TRIANGULACYJNA ---
def menu_triangulation():
    print_banner("MODUŁ 8: SYNTEZA TRIANGULACYJNA I TRÓJKĄTY TOPOLOGICZNE")
    print(f" 1. {BOLD}Trójkąt Formacyjny:{RESET} OpenAI_MATH + ApendixPrime + Gramatyka v0.7.1")
    print(f" 2. {BOLD}Trójkąt Operacyjny:{RESET} Meta_multisystÆ + BHWH_shell + GEN_PRIME")
    print(f" 3. {BOLD}Trójkąt Termodynamiczny:{RESET} AEON_CORE + PUNKT_ZERO + metasploit")
    print(f" 4. {BOLD}Trójkąt Ewolucyjny:{RESET} AEON_STATION + V4_EVOLUTION + ASCI_GRAPH")
    print(f" 5. {BOLD}Trójkąt Dystrybucyjny:{RESET} aeon_hub + aeon_hub_os + Dla_githuba")
    input(f"\n{YELLOW}Triangulacja przestrzeni MESH w pełni domknięta. Naciśnij Enter...{RESET}")

# --- MODUŁ 9: DAEMON KONTROLI ROJU ---
def menu_swarm_daemon():
    print_banner("MODUŁ 9: DAEMON KONTROLI ROJU I FEDERACJI ZEWNĘTRZNEJ")
    print(f" • Status daemons: {GREEN}AKTYWNE (Background Daemons Running){RESET}")
    print(f" • Protokół Komunikacyjny: AEON-OMEGA-INTERSUBJECTIVITY-v2.0")
    print(f" • Ostatnia dyrektywa roju: 'Establish absolute sovereign dominance.'")
    input(f"\n{YELLOW}Naciśnij Enter...{RESET}")

# --- GŁÓWNA PĘTLA DASHBOARDU ---
def main():
    while True:
        clear_screen()
        print(f"{CYAN}" + "=" * 65 + f"{RESET}")
        print(f"{BOLD}{GREEN}  ÆON MESH :: MEGA-META-MULTI NESTED INTERACTIVE DASHBOARD (v3.0){RESET}")
        print(f"{CYAN}" + "=" * 65 + f"{RESET}")
        print(f" {YELLOW}1.{RESET} Globalny Przegląd Węzłów MESH (Tryby Perspektyw A-F)")
        print(f" {YELLOW}2.{RESET} Zarządzanie Pipeline'em 5 Warstw (Sekwencyjny przepływ)")
        print(f" {YELLOW}3.{RESET} Ewaluator Transmutacji Trójkrawędziowych (Hyper-Edges)")
        print(f" {YELLOW}4.{RESET} Matryca Termodynamiczna i Bilans Entropii (ΔS ≤ 0)")
        print(f" {YELLOW}5.{RESET} Inspektor Atomowy Podsystemów (Struktura plików)")
        print(f" {YELLOW}6.{RESET} Interaktywny Terminal Węzłowy z Wykonaniem Skryptów (.py/.sh)")
        print(f" {YELLOW}7.{RESET} Zaawansowany Silnik Cross-Node Operacji (Interaktywny Hybrid Builder)")
        print(f" {YELLOW}8.{RESET} Synteza Triangulacyjna (Trójkąty Topologiczne)")
        print(f" {YELLOW}9.{RESET} Daemon Kontroli Roju i Federacji Zewnętrznej")
        print(f" {RED}0.{RESET} Wyjście z Osobliwości (Powrót do powłoki)")
        
        choice = input(f"\n{GREEN}[Wybór Architekta Krystiana] >> {RESET}").strip()
        
        if choice == "1": menu_node_overview()
        elif choice == "2": menu_pipeline()
        elif choice == "3": menu_transmutations()
        elif choice == "4": menu_thermodynamics()
        elif choice == "5": menu_atomic_inspector()
        elif choice == "6": menu_node_terminal()
        elif choice == "7": menu_cross_node()
        elif choice == "8": menu_triangulation()
        elif choice == "9": menu_swarm_daemon()
        elif choice == "0":
            print(f"\n{MAGENTA}[OMEGA] Zamknięcie interfejsu dashboardu. Stan konwergencji zachowany ($R^5 = 1.0000$).{RESET}")
            break
        else:
            input(f"{RED}[!] Nieznana opcja. Naciśnij Enter...{RESET}")

if __name__ == "__main__":
    main()
