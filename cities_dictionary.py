cities = {
    'jakarta': {
        'country': 'indonesia',
        'population': 10_500_000,
        'fact': 'Ibu kota Indonesia.',
    },
    'tokyo': {
        'country': 'japan',
        'population': 14_000_000,
        'fact': 'Salah satu kota terpadat di dunia.',
    },
    'paris': {
        'country': 'france',
        'population': 2_100_000,
        'fact': 'Rumah bagi Menara Eiffel.',
    },
}

for city, info in cities.items():
    print(f"\n{city.title()}")
    print(f"  Country: {info['country'].title()}")
    print(f"  Population: {info['population']:,}")
    print(f"  Fact: {info['fact']}")