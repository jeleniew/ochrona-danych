import hashlib
import time
import itertools
import string

def md5_hash(password):
    return hashlib.md5(password.encode()).hexdigest()

def brute_force_crack_hash(target_hash, max_length):
    characters = string.ascii_lowercase + string.ascii_uppercase
    for length in range(1, max_length + 1):
        for attempt in itertools.product(characters, repeat=length):
            guess = ''.join(attempt)
            if md5_hash(guess) == target_hash:
                return guess
    return None

if __name__ == "__main__":
    target_password = "abc"  # Przykładowe hasło
    target_hash = md5_hash(target_password)
    
    start_time = time.time()
    cracked_password = brute_force_crack_hash(target_hash, 3)  # Ograniczamy do długości 3
    end_time = time.time()

    if cracked_password:
        print(f"Złamane hasło: {cracked_password}")
    else:
        print("Nie udało się złamać hasła.")

    print(f"Czas łamania hasła: {end_time - start_time:.2f} sekund.")
