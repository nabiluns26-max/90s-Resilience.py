import json
from pathlib import Path 

path = Path('info_pengguna.json')

# Kita minta data dirinya
nama = input("Masukkan nama lengkapmu!\nJawab: ")
usia = input("Tulis usiamu!\nJawab: ")
domisili = input("Masukkan alamat tempat tinggal!\nJawab: ")

# Info disimpan ke dictionary
pengguna = {
    'nama': nama,
    'usia': usia,
    'domisili': domisili,
}

# Dictionary diubah mjd json
contents = json.dumps(pengguna)

# Menulis json ke dalam file
path.write_text(contents)

# Membaca kembali file json
contents = path.read_text()

# Mengubah json mjd dictionary python
pengguna = json.loads(contents)

# Menampilkan ringkasan
print("\nBerikut adalah informasi tentangmu:")
print(f"Nama: {pengguna['nama']}")
print(f"Usia: {pengguna['usia']}")
print(f"Domisili: {pengguna['domisili']}")