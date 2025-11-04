import time

while True:
    print("Escolha uma opção:")
    print("1. Adição")
    print("2. Subtração")
    print("3. Multiplicação")
    print("4. Divisão")
    print("5. Potenciação")
    print("6. Sair")
    opcao = input("\nDigite o número da opção desejada: ")
    if opcao in ['1', '2', '3', '4', '5']:
        a = float(input("Digite o primeiro número: "))
        b = float(input("Digite o segundo número: "))
        if opcao == '1':
            lamb = lambda a,b: a + b
            resultado = lamb(a,b)
            print(f"O resultado da adição é: {resultado}")
        elif opcao == '2':
            lamb = lambda a,b: a - b
            resultado = lamb(a,b)
            print(f"O resultado da subtração é: {resultado}")
        elif opcao == '3':
            lamb = lambda a,b: a * b
            resultado = lamb(a,b)
            print(f"O resultado da multiplicação é: {resultado}")
        elif opcao == '4':
            lamb = lambda a,b: a / b
            resultado = lamb(a,b)
            print(f"O resultado da divisão é: {resultado}") 
        elif opcao == '5':
            lamb = lambda a,b: a ** b
            resultado = lamb(a,b)
            print(f"O resultado da potenciação é: {resultado}")
    elif opcao == '6':
        print("Saindo...")
        time.sleep(1)
        break
    else:
        print("Opção inválida. Tente novamente.")