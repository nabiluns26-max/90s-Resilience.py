import pandas as pd

FILE_NAME = 'C:\Users\Lenovo\Downloads\nNilaiKuliah.csv'
dfNilai = pd.read_csv(FILE_NAME, delimiter=',', encoding='Latin1')
print(type(dfNilai))
print(dfNilai)

# save csv pandas
dfNilai.to_csv('C:\Users\Lenovo\Downloads\nNilaiKuliah_pandas.csv', sep=';', index=False)

nilaiKelasA = pd.read_excel('C:\Users\Lenovo\Downloads\Nilai_KelasA.xlsx', sheet_name='Nilai_A')
print(type(nilaiKelasA))
print(nilaiKelasA)