# Belajar handling error
print("Masukkan dua nagka, kami akan menjumlahkannya!")
try:
    angka_pertama = input("Angka pertama: ")
    angka_kedua = input("Angka kedua: ")
    hasil = int(angka_pertama) + int(angka_kedua)
except ValueError:
    print("Kamu salah memasukkan angka dengan huruf!")
else:
    print(f"Hasil penjumlahan: {hasil}")
