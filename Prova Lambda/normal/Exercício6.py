def calcular_hipotenusa(a, b):
    """Calcula a hipotenusa de um triângulo retângulo dado os catetos."""
    if a < 0 or b < 0:
        raise ValueError("Os catetos não podem ser negativos.")
    return (a**2 + b**2) ** 0.5

while True:
    a = float(input("Digite o comprimento do primeiro cateto (ou um valor negativo para sair): "))
    if a < 0:
        print("Saindo...")
        break
    b = float(input("Digite o comprimento do segundo cateto: "))
    hipotenusa = calcular_hipotenusa(a, b)
    print(f"A hipotenusa do triângulo retângulo é: {hipotenusa:.2f}")
    