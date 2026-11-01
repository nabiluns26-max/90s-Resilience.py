favorite_numbers = {
    'budi': [7, 13],
    'sari': [3, 8, 21],
    'agus': [10],
    'dewi': [5, 9],
    'rina': [2, 4, 6],
}

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    for number in numbers:
        print(f"  {number}")
        