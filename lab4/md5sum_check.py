import hashlib
import sys

def calculate_md5(filename):
    """Oblicza sumę kontrolną MD5 dla danego pliku."""
    md5_hash = hashlib.md5()
    try:
        with open(filename, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                md5_hash.update(byte_block)
        return md5_hash.hexdigest()
    except FileNotFoundError:
        print(f"Plik '{filename}' nie istnieje.")
        return None

def check_md5sum(md5_file):
    """Sprawdza sumy kontrolne MD5 zapisane w pliku."""
    try:
        with open(md5_file, "r") as f:
            for line in f:
                # Ignorowanie pustych linii i komentarzy
                line = line.strip()
                if not line or line.startswith('#'):
                    continue

                # Rozdzielanie sumy kontrolnej i nazwy pliku
                md5sum, filename = line.split(None, 1)
                
                # Obliczanie sumy kontrolnej pliku
                calculated_md5 = calculate_md5(filename)

                if calculated_md5 is None:
                    print(f"Nie można zweryfikować pliku: {filename}")
                    continue

                # Sprawdzanie, czy obliczona suma zgadza się z podaną
                if calculated_md5 == md5sum:
                    print(f"{filename}: OK")
                else:
                    print(f"{filename}: FAILED (expected {md5sum}, got {calculated_md5})")
    except FileNotFoundError:
        print(f"Plik z sumami kontrolnymi '{md5_file}' nie istnieje.")
    except Exception as e:
        print(f"Wystąpił błąd: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Użycie: python3 md5sum_check.py <plik_z_sumami_md5>")
        sys.exit(1)

    md5_file = sys.argv[1]
    check_md5sum(md5_file)
