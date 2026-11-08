from nineleven_module import Pengguna

class Privileges:
    def __init__(self, privileges=None):
        if privileges is None:
            privileges = ['Dapat menambahkan postingan', 'Dapat menghapus postingan', 'Dapat memblokir pengguna']
        self.privileges = privileges

    def tampilkan_privileges(self):
        print("Seorang admin memeiliki kuasa untuk akses:")
        for privilege in self.privileges:
            print(f"- {privilege}")

class Admin(Pengguna):
    def __init__(self, nama_awal, nama_akhir, hobi, profesi):
        super().__init__(nama_awal, nama_akhir, hobi, profesi)
        self.privileges = Privileges()