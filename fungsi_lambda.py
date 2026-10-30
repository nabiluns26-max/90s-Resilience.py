# Fungsi Lambda
def penjumlahan(a):
    return a + 10

x = penjumlahan(100)

a = 100
x =lambda a : a + 10 # a pertama adalah pendefinisian parameter, a kedua adalah penggunaan variabel a pada proses
print(x(74)) # Nilai 5 adalah argument yang dikirim

# Fungsi Lambda dengan dua parameter, dan sebuah baris proses.
x = lambda a, b : a * b
print(x(3, 7))