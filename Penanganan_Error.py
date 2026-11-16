import sys

a = float(input("Input bilangan pertama: "))
b = float(input("Input bilangan kedua: "))

def inputData():
    global a, b 
    a = float(input("Input bilangan pertama: "))
    b = float(input("Input bilangan kedua: "))

benar = True

while benar:
    try:
        inputData()
        hasilbagi = a / b

    except ZeroDivisionError as e:
        print(f"\nBilangan pembagi tidak boleh Nol (0).")
        print("Error message: ", e)
        
    else:
        benar = False
        #inputData()
        #sys.exit(1)

print("Bilangan pertama:", a)
print("Bilangan kedua:", b)
print("a / b =", hasilbagi)

