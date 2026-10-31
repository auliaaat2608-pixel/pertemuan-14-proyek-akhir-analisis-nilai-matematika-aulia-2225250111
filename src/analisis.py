# ==========================================
# Modul: analisis.py
# Tanggung Jawab: Perhitungan matematika & statistik
# ==========================================

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