@echo off

timeout /t 5

taskkill /IM pythonw.exe /F

cd /d "C:\Users\Utilisateur.NAQ22030J002636\Desktop\NFCGuard"

start "" "C:\Users\Utilisateur.NAQ22030J002636\AppData\Local\Programs\Python\Python312\pythonw.exe" main.py