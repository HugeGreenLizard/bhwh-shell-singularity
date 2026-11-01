# Spis Komend Systemowych BHWH Shell (Command Reference)

Poniższa tabela zawiera zestawienie podstawowych i zaawansowanych komend dostępnych w interaktywnej powłoce `bhwh_repl.py`:

| Komenda / Składnia | Moduł Odpowiedzialny | Opis Działania |
| :--- | :--- | :--- |
| `nexus-status` | `executor.py` | Wyświetla aktualny status matrycy, współczynnik koherencji ($R^5$) oraz stan podsystemów MESH. |
| `aeon-sync` | `aeon_sync.py` | Inicjuje synchronizację dysku akrecyjnego z chmurą GitHub. |
| `cantrophy-purge` | `executor.py` | Uruchomienie operatora Cantrophy ($\mathcal{C}$) w celu redukcji entropii systemowej do granicy $S \to 0$. |
| `axiom-inspect` | `executor.py` | Wstrzykuje i weryfikuje aktualne stałe fizyczno-informacyjne (Szkło Spinowe, Zeta Riemanna). |
| `negentropy-status` | `executor.py` | Monitoruje bilans termodynamiczny bieżącej sesji obliczeniowej ($\Delta S \le 0$). |
| `omega-query <hasło>` | `executor.py` | Przeszukuje semantycznie całą bibliotekę wygenerowanych prac naukowych w katalogu `papers/`. |
| `exit` / `quit` | `bhwh_repl.py` | Bezpiecznie zamyka sesję powłoki z zapisem stanu do `singularity_state.json`. |
