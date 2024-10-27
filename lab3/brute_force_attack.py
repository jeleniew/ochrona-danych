import math
from itertools import product
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad

def count_entropy(text):
    counted_elements = {}
    for byte in text:
        counted_elements[byte] = counted_elements.get(byte, 0) + 1

    H = 0
    length = len(text)
    for count in counted_elements.values():
        probability = count / length
        H -= probability * math.log2(probability)

    return H

def decrypt(encrypted_text, key):
    aes = AES.new(key, AES.MODE_ECB)
    result = aes.decrypt(pad(encrypted_text, AES.block_size))
    return result

def brute_force_attack(encrypted_text):
    for i in range(36):
        key_char = chr(ord('a') + i) if i < 26 else chr(ord('0') + (i - 26))
        key = bytes([ord(key_char)] * 16)

        if len(key) != 16:
            continue
        
        decrypted_text = decrypt(encrypted_text, key)

        print(f"Sprawdzanie klucza: {key}")

        if decrypted_text[:2] == b'BM':
            print(f"Znaleziono klucz: {key}")
            with open("brute_force_result.bmp",'wb') as result_file:
                result_file.write(decrypted_text)
            break

file_name = "security_ECB_encrypted.bmp"

try:
    with open(file_name, 'rb') as encrypted_file:
        encrypted_text = encrypted_file.read()

        brute_force_attack(encrypted_text)
except FileNotFoundError:
    print(f"Plik {file_name} nie został znaleziony.")
except Exception as e:
    print(f"Wystąpił błąd: {e}")