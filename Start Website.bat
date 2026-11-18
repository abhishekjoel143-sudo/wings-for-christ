@echo off
cd /d "%~dp0"
if not exist ".venv\Scripts\python.exe" (
  echo Python environment was not found. Check that the .venv folder is inside this project.
  pause
  exit /b 1
)
start /min "Wings for Christ Server" "%~dp0Run Server.cmd"
timeout /t 8 /nobreak >nul
start "" "http://127.0.0.1:8000/"

