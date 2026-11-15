import json
from pathlib import Path

path = Path('angka_favorit.json')

if path.exists():
    angka = json.loads(path.read_text())
    print(f"Angka favoritmu adalah {angka}")

else:
    angka =input("Masukkan nomor favoritmu: ")
    contents = json.dumps(angka)
    path.write_text(contents)
    print("Angka favoritmu berhasil disimpan!")
