dream = ['Netherland', 'Cartenz Pyramid', 'Fluent in English', 'Manchaster']
print(f"\tSomething that I dream:")
print(f"{dream}")

near_future = dream.pop(2)
print(f"\tIn the near future, I wanna be {dream[2]} cuz I think it'll be a game changer in my carrier.")

mount = 'Cartenz Pyramid'
dream.remove(mount)
print(dream)
print(f"\tUntuk mencapai puncak {mount}, aku pikir membutuhkan tidak hanya biaya tapi juga keahlian mendaki yang tinggi sehingga aku hilangkan.")

dream.append('Musisi')
print(dream)

dream.sort()
print(dream)

print(f"Finally I have {len(dream)} dreams and hopefully I can achive in the future.")