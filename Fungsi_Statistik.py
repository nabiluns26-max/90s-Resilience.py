# Fungsi Statistik Nilai Kelas
import statistics as stat
def hitung_statistik_nilai(listNilai):
    total = 0
    for nilai in listNilai:
        total = total + nilai
    rataan =total / len(listNilai)
    #rataan = sum(listNilai)/len(listNilai) # Alternatif cara
    variansi = sum((x-rataan)**2 for x in listNilai) / len(listNilai)
    steddev = variansi ** 0.5 # stddev = math.sqrt(variansi)
    # standardeviasi = stat.stddev(listNilai)
    return total, rataan, steddev

nilai_kelasA = [78, 89, 88, 97, 89]

nilaistat = hitung_statistik_nilai(nilai_kelasA)
totalNilai, rataanNilai, stddevNilai = hitung_statistik_nilai(nilai_kelasA)
print("Total Nilai Kelas : ", totalNilai)
print("Rata-rata Nilai Kelas : ", rataanNilai)
print("Standar Deviasi Nilai Kelas : ", stddevNilai)