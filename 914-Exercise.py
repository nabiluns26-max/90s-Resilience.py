from random import sample

pilihan = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 'a', 'b', 'c', 'd', 'e')

pemenang = sample(pilihan, 4)

print("Setiap tiket yang cocok dengan keempat angka/huruf berikut "
        "akan memenangkan hadiah:")
print(pemenang)