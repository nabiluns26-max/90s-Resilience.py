from pathlib import Path

path = Path('Guest_book.txt')
semua_nama = ""

print("Ketik 'q' kapan saja untuk berhenti.")

while True:
    nama = input("\nTuliskan nama Anda: ")
    if nama == 'q':
        break

    semua_nama += f"{nama}\n"
    print(f"Halo, {nama}! Namma Anda akan dicatat.")

path.write_text(semua_nama)
print("\nSemua nama sudah disimpan dalam Guest_book.txt.")