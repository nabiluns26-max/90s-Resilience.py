# 1. Tarif Parkir Kendaraan di Bandara (Contoh: Jam pertama X, jam berikutnya Y)
def tarif_parkir_bandara(jam, jenis_kendaraan):
    tarif_dasar = 10000 if jenis_kendaraan.lower() == "mobil" else 5000
    tarif_per_jam = 5000 if jenis_kendaraan.lower() == "mobil" else 2000
    if jam <= 1:
        return tarif_dasar
    else:
        return tarif_dasar + ((jam - 1) * tarif_per_jam)

# 2. Menghitung Penggajian (Gaji Pokok + Tunjangan - Pajak)
def hitung_penggajian(gaji_pokok, tunjangan):
    pajak = 0.05 * (gaji_pokok + tunjangan)
    gaji_bersih = (gaji_pokok + tunjangan) - pajak
    return gaji_bersih

# 3. Menghitung BBI (Berat Badan Ideal) dan Status (Rumus Broca sederhana)
def hitung_bbi_dan_status(tinggi_cm, berat_kg, jenis_kelamin):
    # Tinggi dalam cm dikurangi 100, lalu dikurangi 10% (pria) atau 15% (wanita)
    if jenis_kelamin.lower() == "pria":
        bbi = (tinggi_cm - 100) - ((tinggi_cm - 100) * 0.10)
    else:
        bbi = (tinggi_cm - 100) - ((tinggi_cm - 100) * 0.15)
        # Status sederhana
    if berat_kg < bbi - 5:
        status = "Kurus (Underweight)"
    elif berat_kg > bbi + 5:
        status = "Gemuk (Overweight)"
    else:
        status = "Ideal"
        
    return bbi, status

# 4. Tarif Parkir Kendaraan di Stasiun
def tarif_parkir_stasiun(jam):
    # Contoh tarif flat per jam
    tarif_per_jam = 3000
    return jam * tarif_per_jam

# 5. Menentukan Kebutuhan Cairan Pengganti bagi Dehidrasi (Estimasi berdasarkan BB dalam kg * ml tertentu, misal 50ml per kg)
def kebutuhan_cairan_dehidrasi(berat_badan_kg):
    # Rumus estimasi kebutuhan cairan harian/pemulihan (ml)
    return berat_badan_kg * 50

# 6. Menentukan Tarif Tol Kendaraan Berdasarkan Golongan
def tarif_tol(golongan):
    tarif_gol = {
        1: 15000, # Sedan, Jip, Pick-up, Truk Kecil, Bus
        2: 23000, # Truk dengan 2 gardan
        3: 30000, # Truk dengan 3 gardan
        4: 38000, # Truk dengan 4 gardan
        5: 45000  # Truk dengan 5 gardan atau lebih
    }
    return tarif_gol.get(golongan, "Golongan tidak valid")
