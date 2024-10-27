from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
from Crypto.Util.Padding import pad, unpad

def encrypt_file_aes_cbc(input_file, output_file, key):
    """Szyfruje plik za pomocą AES w trybie CBC"""
    iv = get_random_bytes(16)
    
    with open(input_file, 'rb') as f:
        plaintext = f.read()

    padded_plaintext = pad(plaintext, AES.block_size)

    cipher = AES.new(key, AES.MODE_CBC, iv)
    ciphertext = cipher.encrypt(padded_plaintext)

    with open(output_file, 'wb') as f:
        f.write(iv + ciphertext)

def decrypt_file_aes_cbc(input_file, output_file, key):
    """Deszyfruje plik zaszyfrowany AES w trybie CBC"""
    with open(input_file, 'rb') as f:
        iv = f.read(16)
        ciphertext = f.read()

    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_plaintext = cipher.decrypt(ciphertext)

    plaintext = unpad(padded_plaintext, AES.block_size)

    with open(output_file, 'wb') as f:
        f.write(plaintext)

if __name__ == "__main__":
    key = b"key4567890123456"

    encrypt_file_aes_cbc('plainfile.txt', 'encryptedfile.aes', key)
    print("Plik został zaszyfrowany.")

    decrypt_file_aes_cbc('encryptedfile.aes', 'decryptedfile.txt', key)
    print("Plik został odszyfrowany.")
