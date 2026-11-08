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

class Kios_Es_Krim (Restoran):
    def __init__(self, nama, jenis, daftar_rasa):
        super().__init__(nama, jenis)
        self.daftar_rasa = daftar_rasa

    def tampilkan_rasa(self):
        print (f"Daftar rasa di : {self.nama}")
        for rasa in self.daftar_rasa:
            print(f"- {rasa}")

kios = Kios_Es_Krim('Momoyo', 'es krim',['Cokelat', 'Tiramissu', 'Matcha'])

kios.deskripsi_restoran()
kios.tampilkan_rasa()
