import random

def menu():
    """Exibe o menu de opções para o usuário."""
    print("\nEscolha uma opção:")
    print("1. Exercício A")
    print("2. Exercício B")
    print("3. Exercício C")
    print("4. Sair")

while True:
    menu()
    opcao = input("\nDigite o número da opção desejada: ")
    if opcao == '1':
        numero_aleatorio = random.randint(1, 100)
        print(f"\nO número aleatório gerado é: {numero_aleatorio}")
    if opcao == '2':
        nomes = ["Ana", "Bruno", "Carlos", "Diana", "Eduardo"]
        nome_escolhido = random.choice(nomes)
        print(f"\nO nome escolhido aleatoriamente é: {nome_escolhido}")
    if opcao == '3':
        numeros = [1, 2, 3, 4, 5]
        random.shuffle(numeros)
        print(f"\nA lista embaralhada é: {numeros}")
    if opcao == '4':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")