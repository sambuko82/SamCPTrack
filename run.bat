@echo off
title GhostTrack
color 0A

:: Cek Python
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo [!] Python tidak ditemukan. Jalankan install.bat terlebih dahulu!
    pause
    exit
)

:: Cek library
python -c "import requests, phonenumbers" >nul 2>&1
if %errorlevel% neq 0 (
    echo [*] Library belum terinstall. Menginstall otomatis...
    pip install -r requirements.txt
)

python GhostTR.py
pause
