from pathlib import Path 

path = Path('python.txt')

contents = path.read_text()
print("Cara 1: membaca seluruh berkas")
print(contents)

lines = contents.splitlines()
print("Cara 2: mengulang setiap baris")
for line in lines:
    print(line)