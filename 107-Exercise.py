print ("Masukkan dua angka, kami akan menjumlahkannya!")
print ("Ketik 'keluar' untuk keluar")

while True:
    angka_pertama = input("\nAngka pertama: ")
    if angka_pertama == 'keluar':
        break
    angka_kedua = input("Angka kedua: ")
    if angka_kedua == 'keluar':
        break

    try:
        jawab = int(angka_pertama) + int(angka_kedua)
    except ValueError:
        print ("Kamu salah memasukkan huruf dalam operasi!")
    else:
        print (jawab)