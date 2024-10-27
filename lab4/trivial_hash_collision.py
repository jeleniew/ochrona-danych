import hashlib
import itertools

def trivial_hash(data):
    """Funkcja skrótu MD5."""
    return hashlib.md5(data.encode()).hexdigest()

def find_collision(original_text):
    """Znajdź kolizję przez modyfikację białych znaków w tekście."""
    hash_map = {}
    
    # Generowanie białych znaków do przetestowania
    white_space_variants = [' ', '\t', '\n']
    
    # Testujemy modyfikacje białych znaków
    for variant in white_space_variants:
        for i in range(len(original_text)):
            modified_text = original_text[:i] + variant + original_text[i:]
            hashed = trivial_hash(modified_text)
            
            if hashed in hash_map:
                print(f"Kolizja znaleziona:\nTekst 1: {hash_map[hashed]}\nTekst 2: {modified_text}\nHash: {hashed}")
                return
            else:
                hash_map[hashed] = modified_text
    
    print("Nie znaleziono kolizji.")

if __name__ == "__main__":
    original_text = "This is a test."
    find_collision(original_text)
