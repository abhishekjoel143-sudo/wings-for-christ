@echo off
cd /d "%~dp0"
echo Starting the Wings for Christ website...
".venv\Scripts\python.exe" -B "app.py"
echo.
echo The website server stopped. If an error appeared above, take a screenshot of this window.
pause
