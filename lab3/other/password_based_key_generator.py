import os
import hashlib

def generate_key_from_password(password, salt=None, iterations=100000, key_length=32):
    """Generuje klucz na podstawie hasła przy użyciu PBKDF2."""
    if salt is None:
        salt = os.urandom(16)

    key = hashlib.pbkdf2_hmac(
        'sha256',
        password.encode(),
        salt,
        iterations,
        dklen=key_length
    )
    return key, salt

if __name__ == "__main__":
    user_password = input("Podaj hasło: ")
    key, salt = generate_key_from_password(user_password)

    print(f"Wygenerowany klucz: {key.hex()}")
    print(f"Sól (w hex): {salt.hex()}")
