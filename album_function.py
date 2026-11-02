def make_album(artist, title, number_of_songs=None):
    album = {
        "artist": artist,
        "title": title
    }

    if number_of_songs is not None:
        album["number_of_songs"] = number_of_songs

    return album

print(make_album("Taylor Swift", "1989"))
print(make_album("Coldplay", "Parachutes"))
print(make_album("Adele", "25", 11))