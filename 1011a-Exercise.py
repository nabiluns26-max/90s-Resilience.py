# Angka favorit masuk ke json
import json

favnumb = input("Masukkan nomor favoritmu! ")

namafile = 'angka_favorit.json'

with open(namafile,'w') as f:
    json.dump(favnumb, f)

print("Angka favoritmu berhasil disimpan!")
