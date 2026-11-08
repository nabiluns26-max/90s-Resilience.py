from ninetenrestoran import Restoran

r = Restoran("Kharisma Bahari", "masakan nusantara")

r.deskripsi_restoran()

r.tambahan_pelanggan(7)
print(f"JUmlah pelanggan yang terlayani saat ini : {r.jumlah_tersaji}")