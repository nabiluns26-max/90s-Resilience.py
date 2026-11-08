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

class Admin(Pengguna):
    def __init__(self, nama_awal, nama_akhir, hobi, profesi, daftar_privileges):
        super().__init__(nama_awal, nama_akhir, hobi, profesi)
        self.daftar_privileges = daftar_privileges

    def tampilkan_privileges(self):
        print (f"Seorang admin memeiliki kuasa untuk akses:")
        for privileges in self.daftar_privileges:
            print(f"- {privileges}")
    
adm = Admin ('George', 'Russlle', 'Jathilan', 'Pembalap F1', ['Dapat menambahkan postingan', 'Dapat menghapus postingan', 'Dapat memblokir pengguna'])

adm.tampilkan_privileges()