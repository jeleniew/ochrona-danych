import hashlib
import sys

def calculate_md5(filename):
    # Tworzenie obiektu haszującego MD5
    md5_hash = hashlib.md5()
    
    # Otwieranie pliku w trybie binarnym
    with open(filename, "rb") as f:
        # Odczytywanie pliku w blokach
        for byte_block in iter(lambda: f.read(4096), b""):
            md5_hash.update(byte_block)
    
    # Zwracanie heksadecymalnej postaci hasha
    return md5_hash.hexdigest()

if __name__ == "__main__":
    # Sprawdzenie, czy podano nazwę pliku
    if len(sys.argv) != 2:
        print("Użycie: python3 md5sum.py <nazwa_pliku>")
        sys.exit(1)

    filename = sys.argv[1]

    try:
        # Obliczanie sumy kontrolnej MD5
        md5_value = calculate_md5(filename)
        print(f"{md5_value}  {filename}")
    except FileNotFoundError:
        print(f"Plik '{filename}' nie istnieje.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")
