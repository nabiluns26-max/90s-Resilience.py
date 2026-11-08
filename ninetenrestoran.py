class Restoran:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        self.jumlah_tersaji = 0
    
    def deskripsi_restoran(self):
        print (f"Restoran {self.nama} menyediakan {self.jenis}")

    def set_jumlah_tersaji(self, nomor):
        self.jumlah_tersaji = nomor

    def tambahan_pelanggan(self, tambahan):
        self.jumlah_tersaji += tambahan