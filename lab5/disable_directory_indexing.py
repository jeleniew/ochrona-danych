import requests

# URL do chronionego katalogu
DIRECTORY_URL = "http://localhost/nazwa_katalogu/"

def test_directory_indexing():
    try:
        response = requests.get(DIRECTORY_URL)
        if response.status_code == 403:
            print("Indeksowanie katalogu zostało poprawnie wyłączone. Otrzymano kod 403.")
        elif response.status_code == 200:
            print("UWAGA: Katalog nadal jest indeksowany!")
        else:
            print(f"Sprawdzanie katalogu zakończyło się innym kodem: {response.status_code}")
    except requests.ConnectionError:
        print("Nie udało się połączyć z serwerem Apache. Upewnij się, że serwer jest uruchomiony.")

if __name__ == "__main__":
    test_directory_indexing()
