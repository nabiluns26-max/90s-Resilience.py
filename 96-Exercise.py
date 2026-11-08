class Restoran:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
        self.jumlah_tersaji = 0
    
    def deskripsi_restoran():
        print (f"Restoran {self.nama} menyediakan {self.jenis}")

    def set_jumlah_tersaji(self, nomor):
        self.jumlah_tersaji = nomor

    def tambahan_pelanggan(self, tambahan):
        self.jumlah_tersaji += tambahan

class Kios_Es_Krim (Restoran):
    def __init__(self, nama, jenis, rasa):
        super().__init__(nama, rasa)
        self.rasa = rasa

    def deskripsi_kios_es_krim(self):
        print (f"Kios es krim ini menyediakan es krim dengan rasa : {self.rasa}")

rasa_1 = Kios_Es_Krim('Momoyo', 'es krim','Cokelat')
rasa_2 = Kios_Es_Krim('Momoyo', 'es krim', 'Melon')
rasa_3 = Kios_Es_Krim('Momoyo', 'es krim','Stroberi')

for kios in (rasa_1, rasa_2, rasa_3):
    kios.deskripsi_kios_es_krim()
    print ()

