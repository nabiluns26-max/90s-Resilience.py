import csv

with open('nilaiKuliah.csv', 'r', encoding = 'utf-8-sig', newline = '') as file :
    reader = csv.DictReader(file, skipinitialspace=True)

    reader.fieldnames = [name.strip() for name in reader.fieldnames]

    data_mahasiswa = []

    for row in reader:
        # Nilai kosong dianggap 0 
        uk1 = float(row['UK1'] or 0)
        uk2 = float(row['UK2'] or 0)
        uk3 = float(row['UK3'] or 0)
        uk4 = float(row['UK4'] or 0)

        skor_akhir = (
            uk1 * 0.20 +
            uk2 * 0.25 +
            uk3 * 0.20 +
            uk4 * 0.35
        )

        row['SkorAkhir'] = skor_akhir
        data_mahasiswa.append(row)

# Menampilkan skor setiap mahasiswa
for mahasiswa in data_mahasiswa:
    print(
        f"{mahasiswa['NAMA MHS']}: "
        f"{mahasiswa['SkorAkhir']:.2f}"
    )

# Menghitung rata-rata kelas
total_skor = sum(
    mahasiswa['SkorAkhir']
    for mahasiswa in data_mahasiswa
)

rata_rata = total_skor / len(data_mahasiswa)

print(f"\nRata-rata kelas: {rata_rata:.2f}")