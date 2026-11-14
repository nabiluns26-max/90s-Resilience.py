from pathlib import Path 
path_1 = Path('kucing.txt')
path_2 = Path('anjing.txt')

try:
    contents_1 = path_1.read_text(encoding='utf-8')
except FileNotFoundError:
    print(f"Maaf, file {path_1} tidak ditemukan!")
else:
    print(contents_1)
 

try:
    contents_2 = path_2.read_text(encoding='utf-8')
except FileNotFoundError:
    # Gagal dalam diam
    pass
# saya pindahkan anjing.txt ke folder lain
else:
    print(contents_2)

