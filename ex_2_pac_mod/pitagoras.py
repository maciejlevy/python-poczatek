import math

a = float(input("Jaka jest długość pierwszej przyprostąkątnej? "))
b = float(input("Jaka jest długość drugiej przyprostokątnej? "))

def calculate_c(a, b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

c = calculate_c(a, b)
print(f"Długość przyprostokątnej to {c}")