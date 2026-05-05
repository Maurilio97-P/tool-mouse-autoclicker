@echo off
echo Stopping Mouse Clicker...
:: Search for python processes running the mouse_clicker script and kill them
wmic process where "CommandLine like '%%mouse_clicker.py%%'" delete
echo.
echo If the script was running, it has been stopped.
pause
