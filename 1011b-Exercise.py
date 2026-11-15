import json

namafile = 'angka_favorit.json'

with open(namafile) as f:
    favnumb = json.load(f)

print(f"Angka favoritmu adalah {favnumb}!")