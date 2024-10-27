import sys

def check_user_in_db(db_file, username, password):
    # Wczytaj plik bazy danych
    with open(db_file, 'r') as f:
        for line in f:
            # Podziel linię na identyfikator i hasło
            stored_user, stored_hash = line.strip().split(':', 1)
            # Sprawdź, czy identyfikator użytkownika się zgadza
            if stored_user == username:
                # Porównaj hasła (przykład użycia funkcji trivial_hash)
                if trivial_hash(password) == stored_hash:
                    return True
                else:
                    return False
    return False

def trivial_hash(data):
    hash_value = 0
    for char in data:
        hash_value += ord(char)
    return hash_value % 999  # Wartość hasha ograniczona do 999 dla uproszczenia

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print("Użycie: python check_user.py <plik_bazy> <nazwa_użytkownika> <hasło>")
        sys.exit(1)

    db_file = sys.argv[1]
    username = sys.argv[2]
    password = sys.argv[3]

    if check_user_in_db(db_file, username, password):
        print("Użytkownik jest w bazie.")
    else:
        print("Użytkownik nie jest w bazie.")
