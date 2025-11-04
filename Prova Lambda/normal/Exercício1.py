import math
import time

def calcular_area_circulo(a):
    """Calcula a área de um círculo dado o raio."""
    if a < 0:
        raise ValueError("O raio não pode ser negativo.")
    return math.pi * (a ** 2)

def calcular_area_triangulo(a, b):
    """Calcula a área de um triângulo dado a base e a altura."""
    if a < 0 or b < 0:
        raise ValueError("A base e a altura não podem ser negativas.")
    return (a * b) / 2

def calcular_area_retangulo(a, b):
    """Calcula a área de um retângulo dado a largura e o comprimento."""
    if a < 0 or b < 0:
        raise ValueError("A largura e o comprimento não podem ser negativos.")
    return a * b

def menu():
    """Exibe o menu de opções para o usuário."""
    print("\nEscolha uma opção:")
    print("1. Calcular a área de um triângulo")
    print("2. Calcular a área de um retângulo")
    print("3. Calcular a área de um círculo")
    print("4. Sair")

while True:
    menu()
    opcao = input("\nDigite o número da opção desejada: ")
    if opcao == '1':
        a = float(input("Digite a base do triângulo: "))
        b = float(input("Digite a altura do triângulo: "))
        area = calcular_area_triangulo(a, b)
        print(f"A área do triângulo é: {area}")
    elif opcao == '2':
        a = float(input("Digite a largura do retângulo: "))
        b = float(input("Digite o comprimento do retângulo: "))
        area = calcular_area_retangulo(a, b)
        print(f"A área do retângulo é: {area}")
    elif opcao == '3':
        a = float(input("Digite o raio do círculo: "))
        area = calcular_area_circulo(a)
        print(f"A área do círculo é: {area}")
    elif opcao == '4':
        print("Saindo...")
        time.sleep(1)
    else:
        print("Opção inválida. Tente novamente.")
