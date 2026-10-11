#!/bin/sh
cd "$(dirname "$0")" || exit 1
printf "Otworz http://localhost:8080 w przegladarce.\n"
python3 -m http.server 8080 --directory dist
