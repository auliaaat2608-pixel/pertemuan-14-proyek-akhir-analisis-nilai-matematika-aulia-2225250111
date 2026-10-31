# ==========================================
# Modul: utilitas.py
# Tanggung Jawab: Menyediakan fungsi pembantu (helper) umum
# ==========================================

import os

def bersihkan_layar():
    """Membersihkan layar terminal agar tampilan bersih."""
    os.system('cls' if os.name == 'nt' else 'clear')

def tampilkan_garis(panjang=50, karakter="-"):
    """Mencetak garis pemisah untuk mempercantik antarmuka console."""
    print(karakter * panjang)

def format_pesan_sistem(pesan, tipe="INFO"):
    """Menampilkan pesan sistem dengan format yang konsisten."""
    print(f"[{tipe}] {pesan}")