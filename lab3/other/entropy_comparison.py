import math
from collections import Counter

def calculate_entropy(text):
    text_length = len(text)
    H = 0.0
    sign_table = Counter(text)
    
    for sign_count in sign_table.values():
        probability = sign_count/text_length
        H -= probability * math.log2(probability)

    return H

with open('natural_text.txt', 'r', encoding='utf-8') as file:
    natural_text = file.read()

natural_entropy = calculate_entropy(natural_text)
print(f"Entropia tekstu naturalnego: {natural_entropy:.4f}")

with open('encrypted_text.txt', 'r', encoding='utf-8') as file:
    encrypted_text = file.read()

encrypted_entropy = calculate_entropy(encrypted_text)
print(f"Entropia kryptogramu: {encrypted_entropy:.4f}")