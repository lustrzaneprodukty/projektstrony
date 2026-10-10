@echo off
cd /d "%~dp0"
echo Otworz http://localhost:8080 w przegladarce.
python -m http.server 8080 --directory dist
pause
