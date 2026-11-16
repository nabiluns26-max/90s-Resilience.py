def inputdata():
    pilihan = input("Pilih menu: ")
    return pilihan

while True: 
    print("\n===== DAFTAR MENU =====")
    print("1. Makanan")
    print("2. Minuman")
    print("0. Keluar")

    kategori = input("Pilihan kategori: ")

    if kategori == "1":
        print("\n===== MENU MAKANAN =====")
        print("1. Nasi goreng")
        print("2. Mie ayam")
        print("3. Bakso")
        print("0. Kembali")

        try:
            pilihan = inputData()

            if pilihan == "1":
                print("Nasi goreng sedang di proses....")
            elif pilihan == "2":
                print("Mie ayam sedang di proses....")
            elif pilihan == "3":
                print("Bakso sedang di proses....")
            elif pilihan == "0":
                continue
            else: 
                raise ValueError("Pilihan makanan tidak tersedia!")

        except ValueError as e:
            print("Error:", e)

        else:
            print("Pesanan makanan berhasil diproses!")

    elif kategori == "2":
        print("\n===== MENU MINUMAN =====")
        print("1. Air mineral")
        print("2. Es teh")
        print("3. Es jeruk")
        print("0. Kembali")

        try:
            pilihan = inputData()

            if pilihan == "1":
                print("Air mineral sedang di proses....")
            elif pilihan == "2":
                print("Es teh sedang di proses....")
            elif pilihan == "3":
                print("Es jeruk sedang di proses....")
            elif pilihan == "0":
                continue
            else: 
                raise ValueError("Pilihan mainuman tidak tersedia!")

        except ValueError as e:
            print("Error:", e)

        else:
            print("Pesanan minuman berhasil diproses!")


    elif kategori == "0":
         print("\nTerima kasih telah berkunjung!")
        break

    else:
        print("Kategori tidak tersedia!")

