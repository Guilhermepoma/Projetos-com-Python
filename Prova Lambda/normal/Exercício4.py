import time

def selecionar_destino(opcoes):
    """Permite ao usuário selecionar um destino de uma lista de opções."""
    print("Selecione um destino:")
    for i, opcao in enumerate(opcoes, start=1):
        print(f"{i}. {opcao}")
    
    escolha = int(input("Digite o número do destino desejado: "))
    if 1 <= escolha <= len(opcoes):
        return opcoes[escolha - 1]
    else:
        print("Opção inválida.")
        return None
    
def data_hora_viagem():
    """Solicita ao usuário a data e hora da viagem e retorna como um objeto datetime."""
    from datetime import datetime
    data_str = input("Digite a data da viagem (DD/MM/AAAA): ")
    hora_str = input("Digite a hora da viagem (HH:MM): ")
    try:
        data_hora = datetime.strptime(f"{data_str} {hora_str}", "%d/%m/%Y %H:%M")
        return data_hora
    except ValueError:
        print("Data ou hora inválida.")
        return None
    
def numero_passageiros():
    """Solicita ao usuário o número de passageiros e retorna como um inteiro."""
    try:
        num = int(input("Digite o número de passageiros: "))
        if num > 0:
            return num
        else:
            print("O número de passageiros deve ser maior que zero.")
            return None
    except ValueError:
        print("Entrada inválida. Por favor, digite um número inteiro.")
        return None
    
def menu():
    print("\nMenu de Opções:")
    print("1. Selecionar destino")
    print("2. Inserir data e hora da viagem")
    print("3. Inserir número de passageiros")
    print("4. Sair")

destinos = ["São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Salvador", "Brasilía", "Fortaleza", "Manaus", "Balneário Camboriú", "Porto Alegre"]
viagem = {}

while True:
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        destino = selecionar_destino(destinos)
        if destino:
            viagem['destino'] = destino
            print(f"Destino selecionado: {destino}")
    elif opcao == '2': 
        data_hora = data_hora_viagem()
        if data_hora:
            viagem['data_hora'] = data_hora
            print(f"Data e hora da viagem: {data_hora}")
    elif opcao == '3':
        num_passageiros = numero_passageiros()
        if num_passageiros:
            viagem['numero_passageiros'] = num_passageiros
            print(f"Número de passageiros: {num_passageiros}")
    elif opcao == '4':
        print("Saindo...")
        time.sleep(1)
        break
    else: 
        print("Opção inválida. Tente novamente.")