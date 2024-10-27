import crypt
import os

def add_user(filename, username, password):
    # Sprawdzenie, czy plik istnieje
    if os.path.exists(filename):
        # Sprawdzenie, czy użytkownik już istnieje
        with open(filename, 'r') as f:
            for line in f:
                user, _ = line.strip().split(':')
                if user == username:
                    print(f"Użytkownik '{username}' już istnieje.")
                    return
    else:
        print(f"Plik '{filename}' nie istnieje. Zostanie utworzony nowy.")

    # Hashowanie hasła
    hashed_password = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))

    # Dodanie nowego użytkownika do pliku
    with open(filename, 'a') as f:
        f.write(f"{username}:{hashed_password}\n")
    print(f"Użytkownik '{username}' został dodany.")

if __name__ == "__main__":
    # Przykładowe dane
    filename = "users.txt"  # Nazwa pliku bazy
    username = input("Podaj nazwę użytkownika: ")
    password = input("Podaj hasło: ")
    add_user(filename, username, password)
