favorite_places = {
    'budi': ['bandung', 'yogyakarta'],
    'sari': ['bali'],
    'agus': ['malang', 'bromo', 'jakarta'],
}

for name, places in favorite_places.items():
    print(f"\n{name.title()}'s favorite places are:")
    for place in places:
        print(f"  - {place.title()}")