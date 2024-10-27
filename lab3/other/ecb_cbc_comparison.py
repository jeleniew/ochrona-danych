from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

import math
from collections import Counter

def calculate_entropy(text):
    char_counts = Counter(text)
    total_chars = len(text)

    entropy = 0.0
    for count in char_counts.values():
        probability = count / total_chars
        entropy -= probability * math.log2(probability)

    return entropy

def pad(text):
    padding_len = AES.block_size - (len(text) % AES.block_size)
    return text + bytes([padding_len]) * padding_len

def unpad(text):
    padding_len = text[-1]
    return text[:-padding_len]

def encrypt_ecb(text, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(text))

def encrypt_cbc(text, key, iv):
    cipher = AES.new(key, AES.MODE_CBC, iv)
    return cipher.encrypt(pad(text))

with open('plain_text.txt', 'rb') as file:
    plain_text = file.read()

key = get_random_bytes(16)
iv = get_random_bytes(AES.block_size)

encrypted_ecb = encrypt_ecb(plain_text, key)
with open('encrypted_ecb.bin', 'wb') as file:
    file.write(encrypted_ecb)

encrypted_cbc = encrypt_cbc(plain_text, key, iv)
with open('encrypted_cbc.bin', 'wb') as file:
    file.write(encrypted_cbc)

ecb_entropy = calculate_entropy(encrypted_ecb)
cbc_entropy = calculate_entropy(encrypted_cbc)

print(f"Entropia kryptogramu w trybie ECB: {ecb_entropy:.4f}")
print(f"Entropia kryptogramu w trybie CBC: {cbc_entropy:.4f}")