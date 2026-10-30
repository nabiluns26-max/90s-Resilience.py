# Soal 1 dan 2: total, rata-rata, standar deviasi, minimum, maksimum
jumlah = int(input("Berapa banyak bilangan?"))
data = []

for i in range (jumlah):
    angka = float (input (f"Bilangan ke-{i+1}: "))
    data.append(angka)

# total
total = 0
for x in data: 
    total += x

# rata-rata
rata-rata = total / jumlah

#standar deviasi (populasi)
jumlah kuadrat = 0
for x in data:
    jumlah kuadrat += (x - rata) ** 2
std = (jumlah_kuadrat / jumlah) ** 0.5

#minimum dan maksimum
minimum = data[0]
maksimum = data[0]
for x in data:
    if x < minimum:
        minimum = x
    if x > maksimum:
        maksimum = x

print("\n=== Hasil ===")
print("Data         :", data)
print("Total        :", total)
print("Rata-rata    :", rata)
print("Std dev      :", std)
print("Minumum      :", minimum)
print("Maksimum     :", maksimum)