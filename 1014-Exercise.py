import json
from pathlib import Path

def get_stored_username(path):
    """Mendapatkan nama pengguna yang tersimpan."""
    if path.exists():
        username = json.loads(path.read_text())
        return username
    else:
        return None

def get_new_username(path):
    """Meminta nama pengguna baru dan menyimpannya."""
    username = input("Masukkan namamu!\n ")
    contents = json.dumps(username)
    path.write_text(contents)
    return username

def greet_user():
    """Menyapa pengguna."""
    path = Path('username.json')

    username = get_stored_username(path)

    if username:
        correct = input(
        f"Apakah {username} adalah nama pengguna yang benar? (y/n) "
        )

        if correct == 'y':
            print(f"Selamat datang kembali, {username}!")
        else:
            username = get_new_username(path)
            print(f"Kami akan mengingatmu saat kamu kembali, {username}!")

    else:
        username = get_new_username(path)
        print(f"Kami akan mengingatmu saat kamu kembali, {username}!")

greet_user()