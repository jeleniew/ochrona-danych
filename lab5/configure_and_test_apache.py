import subprocess
import os
import time
import requests

# Funkcja uruchamiająca serwer Apache
def start_apache():
    print("Uruchamianie serwera Apache...")
    subprocess.run(["httpd", "-k", "start"], check=True)
    print("Serwer Apache uruchomiony.")

# Funkcja zmieniająca stronę główną
def change_homepage(new_homepage_content):
    # Zakładam, że domyślna strona Apache znajduje się w C:\Program Files\Apache Group\Apache2\htdocs\index.html
    default_homepage = r"C:\Program Files\Apache Group\Apache2\htdocs\index.html"
    
    # Zmiana strony głównej
    print(f"Zmienianie strony głównej na: {new_homepage_content}")
    with open(default_homepage, 'w') as file:
        file.write(f"<html><body><h1>{new_homepage_content}</h1><p>Nowa strona została załadowana.</p></body></html>")
    print("Strona główna została zmieniona.")

# Funkcja testująca, czy strona główna działa
def test_homepage():
    print("Testowanie strony głównej...")
    time.sleep(2)  # Czekaj chwilę, aby serwer mógł wystartować
    try:
        response = requests.get("http://localhost")
        if response.status_code == 200:
            print("Strona główna działa poprawnie.")
        else:
            print(f"Strona główna zwróciła kod: {response.status_code}")
    except requests.exceptions.RequestException as e:
        print(f"Błąd podczas testowania strony: {e}")

if __name__ == "__main__":
    new_homepage_content = "Nowa strona główna"
    
    start_apache()
    change_homepage(new_homepage_content)
    test_homepage()
