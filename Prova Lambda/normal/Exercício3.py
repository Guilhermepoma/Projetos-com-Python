import time

def adicionar_contato(lista, nome_contato, telefone):
    """Adiciona um contato à lista de contatos."""
    lista.append({'nome': nome_contato, 'telefone': telefone})
    print(f"Contato '{nome_contato}' adicionado com sucesso.")

def visualizar_contato(lista, nome_contato):
    """Visualiza um contato na lista de contatos."""
    for contato in lista:
        if contato['nome'].lower() == nome_contato.lower():
            return contato
    return None

def editar_contato(lista, nome_contato, novo_telefone):
    """Edita o telefone de um contato na lista de contatos."""
    for contato in lista:
        if contato['nome'].lower() == nome_contato.lower():
            contato['telefone'] = novo_telefone
            print(f"Contato '{nome_contato}' atualizado com sucesso.")
            return True
    return False

def remover_contato(lista, nome_contato):
    """Remove um contato da lista de contatos."""
    for contato in lista:
        if contato['nome'].lower() == nome_contato.lower():
            lista.remove(contato)
            print(f"Contato '{nome_contato}' removido com sucesso.")
            return True
    return False

def menu():
    """Exibe o menu de opções para o usuário."""
    print("\nEscolha uma opção:")
    print("1. Adicionar um contato")
    print("2. Visualizar um contato")
    print("3. Editar um contato")
    print("4. Remover um contato")
    print("5. Sair")

lista_contatos = []

while True:
    menu()
    opcao = input("\nDigite o número da opção desejada: ")
    if opcao == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        adicionar_contato(lista_contatos, nome, telefone)
    elif opcao == '2':
        nome = input("Digite o nome do contato a ser visualizado: ")
        contato = visualizar_contato(lista_contatos, nome)
        if contato:
            print(f"Contato encontrado: Nome: {contato['nome']}, Telefone: {contato['telefone']}")
        else:
            print(f"Contato '{nome}' não encontrado.")
    elif opcao == '3':
        nome = input("Digite o nome do contato a ser editado: ")
        novo_telefone = input("Digite o novo telefone: ")
        if not editar_contato(lista_contatos, nome, novo_telefone):
            print(f"Contato '{nome}' não encontrado.")
    elif opcao == '4':
        nome = input("Digite o nome do contato a ser removido: ")
        if not remover_contato(lista_contatos, nome):
            print(f"Contato '{nome}' não encontrado.")
    elif opcao == '5':
        print("Saindo...")
        time.sleep(1)
        break
    else:
        print("Opção inválida. Tente novamente.")