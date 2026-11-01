team = ['Arsenal', 'Chelsea', 'Tottenham', 'Brentford', 'Fulham', 'Crystal Palace']
print(f"Team EPL basis London:\n{team}")

# Team yang belum punya trofi pada list yaitu ['Tottenham', 'Brentford', 'Fulham', 'Crystal Palace']
print("Error: Terjadi ketika menjalankan Popping menggunakan acuan urutan awal.\n\tSebagai contoh mengeliminasi tim yang belum memiliki trofi EPL dari data di atas:")

print("\nKesimpulan:\n\tProses Popping terjadi satu per satu. Dalam list, team yang belum memiliki trofi berjajar dari urutan 2-5.\n\tNamun, Popping berjalan satu per satu sehingga akan terdapat pergeseran posisi disetiap Popping.\n\tPenggunaan urutan 2-5 tidak akan terbaca di urutan 4(dalam urutan 2-5) karena dianggap melebihi jumlah data yang ada.")
print("\nInti solusi:\n\tProses popping akan berjalan satu per satu sesuai data urutan terbaru(disetiap popping akan menghasilkan data terbaru).\n\tProses urutannya nanti akan bernomor 2 semua.")

ftmid_team = team.pop(2)
print (team)
print(ftmid_team)

scmid_team = team.pop(3)
print (team)
print(scmid_team)

trermid_team = team.pop(4)
print (team)
print(trmid_team)

frmid_team = team.pop(5)
print (team)
print(frmid_team)



