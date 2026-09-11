@echo off
cd /d "%~dp0"
echo ================================================
echo   IoT-Application-Demo  -  Data Simulator
echo   (Simulates ESP32, reports every 3 seconds)
echo ================================================
echo.
python device\publisher_simulator.py
pause
