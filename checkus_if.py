current_users = ['Ederson', 'Kyle', 'Ruben', 'Stones', 'Sane']
new_users = ['Aguero', 'KYLE', 'Otamendi', 'stones']

current_users_lower = []
for user in current_users:
    current_users_lower.append(user.lower())

for new_user in new_users:
    if new_user.lower() in current_users_lower:
        print(f"{new_user}: username sudah dipakai, masukkan username lain.")
    else:
        print(f"{new_user}: username tersedia.")