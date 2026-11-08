class Pengguna:
    def __init__(self, nama_awal, nama_akhir, hobi, profesi):
        self.nama_awal = nama_awal
        self.nama_akhir = nama_akhir
        self.hobi = hobi
        self.profesi = profesi
        
    def deskripsi_pengguna(self):
        print (f"Nama : {self.nama_awal} {self.nama_akhir}\nNama Panggilan : {self.nama_awal}\nProfesi : {self.profesi}\nHobi : {self.hobi}")
    def sapaan_pengguna(self):
        print (f"Halo {self.nama_awal} kapan {self.hobi} lagi?")

pengguna_1 = Pengguna("Maridjan", "Hartanto", "Golf", "CEO Bank BCA")
pengguna_2 = Pengguna("Surti", "Margonda", "Pilates", "Direktur PT Pertamina")
pengguna_3 = Pengguna("George", "Russle", "Jathilan", "Pembalap F1")

for pengguna in (pengguna_1, pengguna_2, pengguna_3):
    pengguna.deskripsi_pengguna()
    pengguna.sapaan_pengguna()
    print()

