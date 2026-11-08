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
    def penambahan_login_attempts(self):
        self.login_attempts += 1
    def reset_login_attempts(self):
        self.login_attempts = 0

p = Pengguna("George", "Russlle", "Jathilan", "Pembalap F1")

p.penambahan_login_attempts()
p.penambahan_login_attempts()
p.penambahan_login_attempts()
p.penambahan_login_attempts()
p.penambahan_login_attempts()
print(f"Percobaan login : {p.login_attempts}")

p.reset_login_attempts()
print(f"Percobaan login : {p.login_attempts}")