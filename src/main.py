# ==========================================
# Program Gabungan (Tanpa Modul Terpisah)
# ==========================================

def validasi_nilai(nilai):
    """Memeriksa apakah nilai berada dalam rentang valid 0-100."""
    return 0 <= nilai <= 100

def tentukan_status(nilai, kkm=75):
    """Menentukan ketuntasan siswa berdasarkan KKM."""
    if nilai >= kkm:
        return "Tuntas"
    else:
        return "Belum Tuntas"

def hitung_statistik(daftar_nilai, jumlah_tuntas):
    """Menghitung ringkasan data statistik kelas."""
    if not daftar_nilai:
        return {
            "rata_rata": 0,
            "min": 0,
            "max": 0,
            "jumlah_tuntas": 0,
            "total_siswa": 0
        }
    
    total = sum(daftar_nilai)
    rata_rata = total / len(daftar_nilai)
    nilai_min = min(daftar_nilai)
    nilai_max = max(daftar_nilai)
    
    return {
        "rata_rata": rata_rata,
        "min": nilai_min,
        "max": nilai_max,
        "jumlah_tuntas": jumlah_tuntas,
        "total_siswa": len(daftar_nilai)
    }

def main():
    # Data mahasiswa langsung di dalam file main.py
    data_mahasiswa = {
        "A001": {"nama": "Ayu", "nilai": 85},
        "A002": {"nama": "Budi", "nilai": 78},
        "A003": {"nama": "Candra", "nilai": 65},
        "A004": {"nama": "Dewi", "nilai": 92},
        "A005": {"nama": "Eko", "nilai": 45}
    }
    
    KKM = 75
    daftar_nilai_valid = []
    rincian_hasil = []
    jumlah_tuntas = 0
    
    print("=== PROGRAM REKAP DAN ANALISIS NILAI MATEMATIKA ===")
    print("-" * 55)
    
    for nim, info in data_mahasiswa.items():
        nama = info["nama"]
        nilai = info["nilai"]
        
        if validasi_nilai(nilai):
            status = tentukan_status(nilai, KKM)
            daftar_nilai_valid.append(nilai)
            if status == "Tuntas":
                jumlah_tuntas += 1
            
            rincian_hasil.append({
                "nim": nim,
                "nama": nama,
                "nilai": nilai,
                "status": status
            })
            print(f"NIM: {nim} | Nama: {nama:<8} | Nilai: {nilai} | Status: {status}")
        else:
            print(f"NIM: {nim} | Nama: {nama:<8} | Nilai: {nilai} | Status: [INVALID]")
            
    statistik_kelas = hitung_statistik(daftar_nilai_valid, jumlah_tuntas)
    
    print("-" * 55)
    print("STATISTIK KELAS:")
    print(f"- Rata-rata Kelas : {statistik_kelas['rata_rata']:.2f}")
    print(f"- Nilai Minimum   : {statistik_kelas['min']}")
    print(f"- Nilai Maksimum  : {statistik_kelas['max']}")
    print(f"- Jumlah Tuntas   : {statistik_kelas['jumlah_tuntas']} dari {statistik_kelas['total_siswa']} siswa")
    print("-" * 55)

if __name__ == "__main__":
    main()