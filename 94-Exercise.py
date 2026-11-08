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

r = Restoran ("Kharisma Bahari", "masakan Nusantara")

print(f"Pelanggan terlayani : {r.jumlah_tersaji}")

r.jumlah_tersaji = 33
print(f"Pelanggan terlayani : {r.jumlah_tersaji}")

r.set_jumlah_tersaji(33)
print(f"Pelanggan terlayani : {r.jumlah_tersaji}")

r.tambahan_pelanggan(77)
print(f"Pelanggan terlayani : {r.jumlah_tersaji}")
 
