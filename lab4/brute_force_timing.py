import itertools
import time
import string

def brute_force_crack(target_password):
    """Próbuje złamać hasło metodą brutalnej siły."""
    characters = string.ascii_letters  # Małe i duże litery
    length = 1

    while length <= len(target_password):
        for guess in itertools.product(characters, repeat=length):
            guess_password = ''.join(guess)
            if guess_password == target_password:
                return guess_password
        length += 1
    return None

if __name__ == "__main__":
    target_password = input("Podaj hasło do złamania: ")
    
    start_time = time.time()
    found_password = brute_force_crack(target_password)
    end_time = time.time()

    if found_password:
        print(f"Złamano hasło: {found_password}")
    else:
        print("Nie znaleziono hasła.")
    
    print(f"Czas łamania: {end_time - start_time:.2f} sekundy")
