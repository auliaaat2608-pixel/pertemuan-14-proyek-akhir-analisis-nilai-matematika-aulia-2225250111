# ==========================================
# Modul: data_io.py
# Tanggung Jawab: Membaca, validasi, & simpan file
# ==========================================

def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada dalam rentang valid 0-100."""
    return 0 <= nilai <= 100

def baca_data_sampel():
    """Menyiapkan data awal mahasiswa."""
    data_mahasiswa = {
        "A001": {"nama": "Ayu", "nilai": 85},
        "A002": {"nama": "Budi", "nilai": 78},
        "A003": {"nama": "Candra", "nilai": 65},
        "A004": {"nama": "Dewi", "nilai": 92},
        "A005": {"nama": "Eko", "nilai": 45}
    }
    return data_mahasiswa

def simpan_laporan(path_file, hasil_statistik, rincian_siswa):
    """Menulis hasil rekap dan statistik ke dalam file teks."""
    try:
        with open(path_file, "w", encoding="utf-8") as f:
            f.write("=== LAPORAN REKAP DAN ANALISIS NILAI KELAS ===\n")
            f.write("-" * 45 + "\n")
            for item in rincian_siswa:
                f.write(f"NIM: {item['nim']} | Nama: {item['nama']} | Nilai: {item['nilai']} | Status: {item['status']}\n")
            f.write("-" * 45 + "\n")
            f.write("STATISTIK KELAS:\n")
            f.write(f"- Rata-rata Kelas : {hasil_statistik['rata_rata']:.2f}\n")
            f.write(f"- Nilai Minimum   : {hasil_statistik['min']}\n")
            f.write(f"- Nilai Maksimum  : {hasil_statistik['max']}\n")
            f.write(f"- Jumlah Tuntas   : {hasil_statistik['jumlah_tuntas']} dari {hasil_statistik['total_siswa']} siswa\n")
        print(f"\n[Sukses] Laporan berhasil disimpan ke '{path_file}'")
    except IOError:
        print(f"[Error] Gagal menyimpan file ke {path_file}")