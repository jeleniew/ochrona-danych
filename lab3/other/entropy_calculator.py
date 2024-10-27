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

if __name__ == "__main__":
    sample_text = "To jest przykładowy tekst do obliczenia entropii."
    
    entropy = calculate_entropy(sample_text)
    
    print(f"Entropia tekstu: {entropy:.4f}")
