@echo off
title GhostTrack - Auto Installer
color 0A

echo.
echo  ________               __      ______                __
echo / ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__
echo / / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ `/ ___/ //_/
echo / /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,^<
echo \____/_/ /_/\____/____/\__/     /_/ /_/   \__,_/\___/_/|_|
echo.
echo          [ AUTO INSTALLER - WINDOWS VERSION ]
echo.

:: Cek apakah Python sudah terinstall
echo [*] Mengecek Python...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo.
    echo [!] Python belum terinstall di komputermu!
    echo.
    echo     Langkah install Python:
    echo     1. Buka browser
    echo     2. Pergi ke: https://www.python.org/downloads/
    echo     3. Klik tombol "Download Python"
    echo     4. Jalankan file yang didownload
    echo     5. PENTING: Centang "Add Python to PATH"
    echo     6. Klik Install Now
    echo     7. Setelah selesai, jalankan file install.bat ini lagi
    echo.
    pause
    exit
)

echo [+] Python ditemukan!
python --version

:: Upgrade pip
echo.
echo [*] Upgrade pip ke versi terbaru...
python -m pip install --upgrade pip

:: Install requirements
echo.
echo [*] Menginstall semua library yang dibutuhkan...
pip install -r requirements.txt

if %errorlevel% neq 0 (
    echo.
    echo [!] Gagal install library. Coba jalankan sebagai Administrator.
    echo     Klik kanan install.bat lalu pilih "Run as administrator"
    pause
    exit
)

echo.
echo ================================================
echo    INSTALASI SELESAI! Tool siap digunakan.
echo ================================================
echo.
echo  Untuk menjalankan lagi berikutnya:
echo  Double-click file run.bat
echo.
echo [*] Menjalankan GhostTrack...
timeout /t 2 /nobreak >nul
python GhostTR.py
pause
