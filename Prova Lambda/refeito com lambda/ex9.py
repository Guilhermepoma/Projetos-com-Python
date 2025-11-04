import math
import time

raiz = lambda x: math.sqrt(x)
seno = lambda sen: math.sin(sen)
arredondado_cima = lambda cima: math.ceil(cima)
arredondado_baixo = lambda baixo: math.floor(baixo)

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
        resultado = raiz(numero)
        print(f"A raiz quadrada é: {resultado}")
    elif opcao == '2':
        numero = float(input("Digite um número positivo: "))
        resultado = seno(numero)
        print(f"O valor de seno é: {resultado}")
    elif opcao == '3':
        numero = float(input("Digite um número positivo: "))
        resultado = arredondado_cima(numero)
        print(f"Número arredondado pra cima: {resultado}")
    elif opcao == '4':
        numero = float(input("Digite um número positivo: "))
        resultado = arredondado_baixo(numero)
        print(f"Número arredondado pra cima: {resultado}")
    elif opcao == '5':
        print("Saindo...")
        time.sleep(0.5)
        break
    else:
        print("Opção inválida. Tente novamente.")