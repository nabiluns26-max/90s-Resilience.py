from pathlib import Path

nama = input("Masukkan nama anda: ")

path = Path('Guest.text')
path.write_text(nama)

print(f"terimakasih {nama}! Nama anda telah masuk dalam Guest.text")
