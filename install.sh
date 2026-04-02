#!/bin/bash
# ============================================
# GhostTrack - Auto Install & Run Script
# Jalankan sekali, semua otomatis terpasang
# ============================================

HIJAU='\033[1;32m'
MERAH='\033[1;31m'
KUNING='\033[1;33m'
PUTIH='\033[1;37m'
RESET='\033[0m'

echo -e "${HIJAU}"
echo "  ________               __      ______                __  "
echo " / ____/ /_  ____  _____/ /_    /_  __/________ ______/ /__"
echo "/ / __/ __ \/ __ \/ ___/ __/_____/ / / ___/ __ \`/ ___/ //_/"
echo "/ /_/ / / / / /_/ (__  ) /_/_____/ / / /  / /_/ / /__/ ,<  "
echo "\____/_/ /_/\____/____/\__/     /_/ /_/   \__,_/\___/_/|_| "
echo -e "${PUTIH}          [ AUTO INSTALLER BY SAMCPTRACK ]${RESET}"
echo ""

# Cek Python3
echo -e "${KUNING}[*] Mengecek Python3...${RESET}"
if ! command -v python3 &>/dev/null; then
    echo -e "${MERAH}[!] Python3 tidak ditemukan. Install dulu: sudo apt install python3${RESET}"
    exit 1
fi
echo -e "${HIJAU}[+] Python3 ditemukan: $(python3 --version)${RESET}"

# Cek pip
echo -e "${KUNING}[*] Mengecek pip...${RESET}"
if ! command -v pip3 &>/dev/null; then
    echo -e "${KUNING}[*] Menginstall pip...${RESET}"
    sudo apt install python3-pip -y
fi
echo -e "${HIJAU}[+] pip ditemukan${RESET}"

# Buat virtual environment
echo -e "${KUNING}[*] Membuat virtual environment (venv)...${RESET}"
python3 -m venv venv
echo -e "${HIJAU}[+] Virtual environment berhasil dibuat${RESET}"

# Aktifkan venv
source venv/bin/activate

# Upgrade pip
echo -e "${KUNING}[*] Upgrade pip ke versi terbaru...${RESET}"
pip install --upgrade pip

# Install requirements
echo -e "${KUNING}[*] Menginstall semua library yang dibutuhkan...${RESET}"
pip install -r requirements.txt

echo ""
echo -e "${HIJAU}================================================${RESET}"
echo -e "${HIJAU}   INSTALASI SELESAI! Tool siap digunakan.${RESET}"
echo -e "${HIJAU}================================================${RESET}"
echo ""
echo -e "${PUTIH} Untuk menjalankan lagi berikutnya, ketik:${RESET}"
echo -e "${HIJAU}   bash run.sh${RESET}"
echo ""

# Langsung jalankan tool
echo -e "${KUNING}[*] Menjalankan GhostTrack...${RESET}"
sleep 2
python3 GhostTR.py
