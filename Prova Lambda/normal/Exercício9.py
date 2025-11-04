import time
import math

def raiz_quadrada(n):
    """Calcula a raiz quadrada de um número positivo."""
    if n < 0:
        raise ValueError("O número não pode ser negativo.")
    return math.sqrt(n)

def valor_seno(n):
    if n < 0:
        raise ValueError("O número não pode ser negativo.")
    return math.sin(n)

def arredondamento_cima(n):
    if n < 0:
        raise ValueError("O número não pode ser negativo.")
    return math.ceil(n)

def arredondamento_baixo(n):
    if n < 0:
        raise ValueError("O número não pode ser negativo.")
    return math.floor(n)
    
def menu():
    """Exibe o menu de opções para o usuário."""
    print("\nEscolha uma opção:")
    print("1. Calcular raiz quadrada")
    print("2. Calcular valor do Seno")
    print("3. Arredondar (para cima)")
    print("4. Arredondar (para baixo)")
    print("5. Sair")

while True:
    menu()
    opcao = input("\nDigite o número da opção desejada: ")
    if opcao == '1':
        numero = float(input("Digite um número positivo: "))
        resultado = raiz_quadrada(numero)
        print(f"A raiz quadrada é: {resultado}")
    elif opcao == '2':
        numero = float(input("Digite um número positivo: "))
        resultado = valor_seno(numero)
        print(f"O valor de seno é: {resultado}")
    elif opcao == '3':
        numero = float(input("Digite um número positivo: "))
        resultado = arredondamento_cima(numero)
        print(f"Número arredondado pra cima: {resultado}")
    elif opcao == '4':
        numero = float(input("Digite um número positivo: "))
        resultado = arredondamento_baixo(numero)
        print(f"Número arredondado pra cima: {resultado}")
    elif opcao == '5':
        print("Saindo...")
        time.sleep(1)
        break
    else:
        print("Opção inválida. Tente novamente.")
    