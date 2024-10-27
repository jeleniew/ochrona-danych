import crypt

def create_htpasswd_file(filename, username, password):
    # Generowanie hasła
    hashed_password = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))
    # Zapisywanie użytkownika do pliku
    with open(filename, 'a') as f:
        f.write(f"{username}:{hashed_password}\n")

if __name__ == "__main__":
    # Przykładowe dane
    filename = "users.txt"  # Nazwa pliku bazy
    create_htpasswd_file(filename, "user1", "password123")
    create_htpasswd_file(filename, "user2", "password456")
