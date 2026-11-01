pet_1 = {'kind': 'kucing', 'owner': 'Gara'}
pet_2 = {'kind': 'anjing', 'owner': 'Orochimaru'}
pet_3 = {'kind': 'kelinci', 'owner': 'Nobita'}

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    print(f"{pet['owner']} punya {pet['kind']}.")