from random import sample

pilihan = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

tiket_ku = [2, 5, 'c', 7]

percobaan = 0
while True:
    percobaan += 1
    pemenang = sample(pilihan, 4)
    if set(pemenang) == set(tiket_ku):
        break

print(f"Tiket {tiket_ku} menang setelah melakukan percobaan {percobaan} kali pengundian.")