person_1 = {'first_name': 'Sasuke', 'last_name': 'Santoso', 'age': 20, 'city': 'Bandung'}
person_2 = {'first_name': 'Naruto', 'last_name': 'Wulandari', 'age': 21, 'city': 'Medan'}
person_3 = {'first_name': 'Kakashi', 'last_name': 'Pratama', 'age': 19, 'city': 'Surabaya'}

people = [person_1, person_2, person_3]

for person in people:
    full_name = f"{person['first_name']} {person['last_name']}"
    print(f"{full_name}, {person['age']} tahun, tinggal di {person['city']}.")