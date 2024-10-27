import string
import math

def create_stream(key):
    S=list(range(256))
    j = 0
    key_length = len(key)

    for i in range(256):
        j = (j + S[i] + ord(key[i % key_length])) % 256
        S[i], S[j] = S[j], S[i]

    return S

def generate_output(S, length):
    i = j = 0
    key_stream = []

    for _ in range(length):
        i = (i + 1) % 256
        j = (j + S[i]) % 256
        S[i], S[j] = S[j], S[i]
        key_stream.append(S[(S[i] + S[j]) % 256])

    return key_stream

def encrypt(text, key):
    S = create_stream(key)
    key_stream = generate_output(S, len(text))
    encrypted = []

    for p, k in zip(text, key_stream):
        encrypted_value = p ^ k
        encrypted.append(chr(encrypted_value))
    return ''.join(encrypted)

def count_entropy(text):
    counted_elements = {}
    for byte in text:
        if byte in counted_elements:
            counted_elements[byte] += 1
        else:
            counted_elements[byte] = 1

    H = 0
    for count in counted_elements.values():
        probability = count / len(text)
        H += probability * math.log2(probability)

    return -H

with open('crypto.rc4', 'rb') as file:
    text = file.read()

with open('found_key.txt', 'w', encoding='utf-8') as output_file:
    for first_sign in string.ascii_lowercase:
        for second_sign in string.ascii_lowercase:
            for third_sign in string.ascii_lowercase:
                key = [first_sign, second_sign, third_sign]
                encrypted = encrypt(text, key)
                if count_entropy(encrypted) < 5:
                    print(key)
                    output_file.write(encrypted)
                    break
