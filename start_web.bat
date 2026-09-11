@echo off
cd /d "%~dp0"
echo ================================================
echo   IoT-Application-Demo  -  Web Server
echo   Open in browser : http://localhost:5000
echo   (Keep this window OPEN, run simulator separately)
echo ================================================
echo.
python backend\app.py
echo.
echo [Exited] If there is an error above, run this first:
echo pip install -r requirements.txt -i https://pypi.tuna.tsinghua.edu.cn/simple
pause
