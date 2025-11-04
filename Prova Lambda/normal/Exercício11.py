from datetime import datetime, timedelta

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
        data_hora_atual = datetime.now()
        data_hora_formatada = data_hora_atual.strftime("%d/%m/%Y %H:%M:%S")
        print(f"A data e hora atual é:\n{data_hora_formatada}")
    elif opcao == '2':
        ano_atual = datetime.now().year
        ano_nascimento = int(input("Digite o seu ano de nascimento: "))
        idade = ano_atual - ano_nascimento
        print(f"Você tem {idade} anos.")
    elif opcao == '3':
        data_str = input("Digite uma data qualquer (DD/MM/AAAA): ")
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            nova_data = data + timedelta(days=15)
            print(f"A nova data, após adicionar 15 dias, é: {nova_data.strftime('%d/%m/%Y')}")
        except ValueError:
            print("Formato de data inválido. Tente novamente.")
    elif opcao == '4':
        print("Saindo do programa...")
        break
    else:
        print("Opção inválida. Tente novamente.")