from openpyxl import load_workbook

# Membuka file Excel
workbook = load_workbook('Nilai_KelasA(prokom exercise).xlsx')

# Memilih sheet
sheet = workbook['Nilai_C']

# Menyimpan data ke dalam list
data_mahasiswa = []

for row in sheet.iter_rows(values_only=True):
    data_mahasiswa.append(list(row))

# Membaca seluruh baris nilai
for mahasiswa in data_mahasiswa:
    print(mahasiswa)