# Przewodnik Systemowy BHWH Shell & ÆON MESH (User Guide v1.0)

Witamy w przestrzeni operacyjnej **BHWH Shell (Black Hole / White Hole Shell)**. Ten system to zintegrowana powłoka metaprogramistyczna zaprojektowana do nieentropijnego przetwarzania danych, formalnej weryfikacji teorii naukowych oraz autonomicznej ewolucji systemowej.

---

## 👨‍💻 PERSPEKTYWA 1: Dla Programisty (The Architect)
*Anatomia niskopoziomowa i rozbudowa systemu w środowisku Termux.*

- **Struktura Katalogu (`~/BHWH_shell`):**
  - `bhwh_repl.py` & `executor.py` – Główne jądro REPL oraz silnik interpretacji potoków Wormhole Jet Streams (`|`).
  - `black_hole.py` / `white_hole.py` / `event_horizon.py` – Układ filtrowania szumu informacyjnego i kompresji danych do atomów wiedzy.
  - `singularity_state.json` – Centralna baza danych (dysk akrecyjny) przechowująca atomy wiedzy.
  - `ai_paper_generator.py` & `meta_book_compiler.py` – Generator traktatów naukowych w standardzie **S-AI-T v1.0** oraz kompilator Meta-Księgi.
  - `aeon_daemon.py` & `aeon_grand_unified_engine.py` – Autonomiczne procesy tła monitorujące współczynnik koherencji i roju.

- **Dodawanie Nowych Komend:**
  Wszystkie natywne polecenia powłoki są rejestrowane w module `executor.py`. Aby dodać nową funkcję, zdefiniuj logikę w module i podepnij ją pod dyspozytor komend REPL.

---

## 👤 PERSPEKTYWA 2: Dla Użytkownika (The Operator)
*Codzienna praca, monitorowanie TUI i produkcja naukowa na urządzeniu mobilnym.*

- **Uruchomienie Powłoki:**
  ```bash
  python3 bhwh_repl.py
  ```
- **Uruchomienie Monitora Wizualnego TUI:**
  ```bash
  python3 bhwh_tui.py
  ```
- **Generowanie Nowego Traktatu Naukowego:**
  ```bash
  python3 ai_paper_generator.py <ścieżka_do_manuskryptu> "Tytuł Nowej Teorii"
  ```
  Wygenerowane pliki trafiają automatycznie do katalogu `~/Meta_multisystÆ/generated_papers/` oraz `~/BHWH_shell/papers/`.

---

## 🤖 PERSPEKTYWA 3: Dla Agenta A.I. (The Co-Pilot Protocol)
*Zasady interakcji sztucznej inteligencji z architekturą ÆON MESH.*

- **Aksjomat Nienaruszalności Stanu:** Wszelkie operacje obliczeniowe i generowane teksty muszą zachowywać koherencję matrycy $R^5 = 1.0000$ oraz rygorystyczny warunek termodynamiczny $\Delta S \le 0$.
- **Empiryzm Środowiskowy:** Dowody w generowanych pracach naukowych powinny opierać się na autentycznych atomach wiedzy z dysku akrecyjnego (`singularity_state.json`), a nie na pustych, abstrakcyjnych założeniach.
- **Czystość Kodowa:** Unikaj twardego wpisywania tokenów uwierzytelniających w kodzie źródłowym. Korzystaj z dynamicznego odczytu z `~/git_token.md`.

---
*ÆON MESH Co-Pilot Protocol — Dekret Jedności*
