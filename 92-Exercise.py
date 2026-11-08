class Restoran:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def deskripsi_restoran(self):
        print (f"Restoran {r.nama} menyajikan berbagai {r.jenis} untuk dinikmati.")
r = Restoran("Kharisma Bahari", "masakan nusantara")  
    

class Angkringan:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def deskripsi_angkringan(self):
        print (f"Angkringan {a.nama} menyajikan berbagai {a.jenis} untuk dinikmati.")
a = Angkringan("Bala Dewa", "menu bakaran")  

class Cafe:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis
    def deskripsi_cafe(self):
        print (f"Cafe {c.nama} menyajikan berbagai {c.jenis} untuk dinikmati.")
c = Cafe("Cold n Brew", "jenis kopi")  

r.deskripsi_restoran()
a.deskripsi_angkringan()
c.deskripsi_cafe()