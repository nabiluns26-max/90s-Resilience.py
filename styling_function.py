def favorite_book(title):
    """Display a message about a favorite book."""
    print(f"One of my favorite books is {title}.")


def describe_city(city, country="Indonesia"):
    """Display the country where a city is located."""
    print(f"{city.title()} is in {country.title()}.")


def make_album(artist, title):
    """Create a dictionary describing a music album."""
    album = {
        "artist": artist,
        "title": title
    }

    return album


favorite_book("Alice in Wonderland")

describe_city("Surakarta")

print(make_album("Coldplay", "Parachutes"))