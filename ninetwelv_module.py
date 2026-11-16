class Pengguna:
    def __init__(self, nama_awal, nama_akhir, hobi, profesi):
        self.nama_awal = nama_awal
        self.nama_akhir = nama_akhir
        self.hobi = hobi
        self.profesi = profesi
        self.login_attempts = 0
        
    def deskripsi_pengguna(self):
        print (f"Nama : {self.nama_awal} {self.nama_akhir}\nNama Panggilan : {self.nama_awal}\nProfesi : {self.profesi}\nHobi : {self.hobi}")
    def sapaan_pengguna(self):
        print (f"Halo {self.nama_awal} kapan {self.hobi} lagi?")