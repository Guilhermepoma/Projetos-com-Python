import math

formula = lambda c1, c2: (c1 ** 2) + (c2 ** 2)

a = float(input("Digite o 1° cateto: "))
b = float(input("Digite o 2° cateto: "))

soma_quadrados = formula(a, b)
hipotenusa = math.sqrt(soma_quadrados)

print(f"A hipotenusa é: {hipotenusa}")