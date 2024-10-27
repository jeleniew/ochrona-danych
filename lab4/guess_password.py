import crypt
import itertools
import string

def load_htpasswd_file(filename):
    """Wczytuje dane użytkowników z pliku htpasswd."""
    users = {}
    with open(filename, 'r') as file:
        for line in file:
            username, hashed_password = line.strip().split(':')
            users[username] = hashed_password
    return users

def guess_passwords(users):
    """Zgaduj hasła dla podanych użytkowników."""
    characters = string.ascii_lowercase  # Małe litery
    for username, hashed_password in users.items():
        for length in range(1, 4):  # Długość haseł 1-3
            for guess in itertools.product(characters, repeat=length):
                guess_password = ''.join(guess)
                if crypt.crypt(guess_password, hashed_password) == hashed_password:
                    print(f"Zgadnięto hasło dla użytkownika '{username}': {guess_password}")

if __name__ == "__main__":
    htpasswd_file = "users.txt"  # Nazwa pliku bazy htpasswd
    users = load_htpasswd_file(htpasswd_file)
    guess_passwords(users)
