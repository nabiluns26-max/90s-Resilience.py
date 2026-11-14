from pathlib import Path 

path = Path('Guest.txt')
contents = path.read_text(encoding='utf-8')

#lines = contents.splitlines()
#for line in lines:
    #print(line)     #Disederhanakan menjadi

for line in contents.splitlines():
    print(line)