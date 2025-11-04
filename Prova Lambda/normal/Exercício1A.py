import time

def adicao(a, b):
    return a + b

def subtracao(a, b):
    return a - b

def multiplicacao(a, b):
    return a * b

def divisao(a, b):
    if b == 0:
        raise ValueError("O divisor não pode ser zero.")
    return a / b

def potenciacao(a, b):
    return pow(a, b)

def menu():
    """Exibe o menu de opções para o usuário."""
    print("\nEscolha uma opção:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Sair")

while True:
    menu()
    opcao = input("\nDigite o número da opção desejada: ")
    if opcao in ['1', '2', '3', '4', '5']:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if opcao == '1':
            resultado = adicao(a, b)
            print(f"O resultado da adição é: {resultado}")
        elif opcao == '2':
            resultado = subtracao(a, b)
            print(f"O resultado da subtração é: {resultado}")
        elif opcao == '3':
            resultado = multiplicacao(a, b)
            print(f"O resultado da multiplicação é: {resultado}")
        elif opcao == '4':
            resultado = divisao(a, b)
            print(f"O resultado da divisão é: {resultado}") 
        elif opcao == '5':
            resultado = potenciacao(a, b)
            print(f"O resultado da potenciação é: {resultado}")
    elif opcao == '6':
        print("Saindo...")
        time.sleep(1)
        break
    else:
        print("Opção inválida. Tente novamente.")