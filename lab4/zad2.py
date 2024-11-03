import hashlib
import random
import string

def generate_random_password(length=8):
    """Generuje losowe hasło o zadanej długości."""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def md5_prefix(password, prefix_length=5):
    """Oblicza hash MD5 hasła i zwraca pierwsze `prefix_length` znaków."""
    return hashlib.md5(password.encode()).hexdigest()[:prefix_length]

def find_collision(prefix_length=5, max_attempts=100000):
    """Znajduje dwa różne hasła, których hasze MD5 mają te same pierwsze `prefix_length` znaków."""
    hashes = {}
    
    for _ in range(max_attempts):
        password = generate_random_password()
        hash_prefix = md5_prefix(password, prefix_length)
        
        if hash_prefix in hashes:
            # Sprawdza, czy mamy kolizję z różnymi hasłami
            if hashes[hash_prefix] != password:
                print(f"Znaleziono kolizję dla pierwszych {prefix_length} znaków:")
                print(f"Hasło 1: {hashes[hash_prefix]}, Hash: {md5_prefix(hashes[hash_prefix], prefix_length)}")
                print(f"Hasło 2: {password}, Hash: {hash_prefix}")
                return hashes[hash_prefix], password
        
        hashes[hash_prefix] = password

    print("Nie znaleziono kolizji.")
    return None, None

# Przykład wywołania funkcji
find_collision(5)
