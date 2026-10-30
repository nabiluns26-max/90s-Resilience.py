# Topik konversi suhu CR
def konversi_celcius_ke_reamur(celcius):
    reamur = celcius * 0.8
    return reamur

r = konversi_celcius_ke_reamur(30)
print(r)

#Topik konversi suhu RF
def konversi_reamur_ke_fahrenheit(reamur):
    fahrenheit = reamur * 2,25 + 32
    return fahrenheit

r = konversi_reamur_ke_fahrenheit(30)
print(r)

#Topik konversi CF
def konversi_celcius_ke_fahrenheit(celcius):
    fahrenheit = celcius * 2,25 + 32
    return fahrenheit

r = konversi_celcius_ke_fahrenheit(30)
print(r)

#Topik konversi FC
def konversi_fahrenheit_ke_celcius(fahrenheit):
    celcius = fahrenheit - 32 * 1,8
    return celcius

r = konversi_fahrenheit_ke_celcius(30)
print(r)


#Topik konversi RC
def konversi_reamur_ke_celcius(reamur):
    celcius = reamur * 1,2
    return celcius

r = konversi_reamur_ke_celcius(30)
print(r)


#Topik konversi FR
def konversi_fahrenheit_ke_reamur(fahrenheit):
    reamur = fahrenheit * 2,25 + 32
    return reamur

r = konversi_fahrenheit_ke_reamur(30)
print(r)