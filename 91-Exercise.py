class Restoran:
    def __init__(self, nama, jenis):
        self.nama = nama
        self.jenis = jenis

    def deskripsi_restoran(self):
        print(f"{self.nama} merupakan restoran favorit mahasiswa UNS yang menyediakan {self.jenis}.")

    def restoran_buka(self):
        print(f"{self.nama} sudah buka!")
    
r = Restoran("Kharisma Bahari", "masakan nusantara")   
print(f"Nama restoran: {r.nama}\nJenis: {r.jenis}")    

print (f"Letak restoran {r.nama} ada di Jl.Kartika, Jebres.")
print (f"Restoran {r.nama} menyajikan berbagai {r.jenis} untuk dinikmati.")
r.deskripsi_restoran()
r.restoran_buka()

