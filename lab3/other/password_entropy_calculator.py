import math

N = 26  # liczba dostępnych znaków (a-z)
target_entropy = 256  # docelowa entropia w bitach

# Oblicz długość hasła
L = target_entropy / math.log2(N)
print(f"Aby osiągnąć entropię {target_entropy} bitów, hasło powinno mieć co najmniej {math.ceil(L)} znaków.")
