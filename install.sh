#!/usr/bin/env bash
# ==============================================================================
# 🕳️ BHWH SHELL — INSTALATOR GLOBALNY (POINT 3)
# Tworzy dowiązanie symboliczne, umożliwiając uruchomienie powłoki komendą 'bhwh'
# ==============================================================================

SHELL_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPL_SCRIPT="$SHELL_DIR/bhwh_repl.py"
INSTALL_BIN="$PREFIX/bin/bhwh"

echo "========================================================"
echo "      BHWH SHELL — INSTALACJA W ŚRODOWISKU SYSTEMOWYM   "
echo "========================================================"

# Nadanie uprawnień wykonywalności skryptowi REPL
chmod +x "$REPL_SCRIPT"

# Utworzenie linku symbolicznego w $PREFIX/bin (Termux / Linux standard)
if [ -f "$INSTALL_BIN" ] || [ -L "$INSTALL_BIN" ]; then
    rm -f "$INSTALL_BIN"
fi

ln -s "$REPL_SCRIPT" "$INSTALL_BIN"
chmod +x "$INSTALL_BIN"

echo "  [✔] Skrypt REPL zaktualizowany i gotowy."
echo "  [✔] Utworzono globalną komendę systemową: 'bhwh'"
echo "========================================================"
echo "  🚀 Instalacja zakończona sukcesem!"
echo "  Teraz możesz wpisać 'bhwh' z dowolnego miejsca w terminalu."
echo "========================================================"
