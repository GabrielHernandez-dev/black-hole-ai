@echo off
docker start open-webui
timeout /t 15 /nobreak >nul
start http://localhost:3000