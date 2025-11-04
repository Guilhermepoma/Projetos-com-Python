import time

def menu():
    """
    Exibe o menu de opções para o usuário.
    Esta função não precisa de retorno, apenas imprime na tela.
    """
    print("\nEscolha uma opção:")
    print("1. Adicionar um elemento à lista")
    print("2. Visualizar a posição de um elemento na lista")
    print("3. Atualizar um elemento na lista")
    print("4. Remover um elemento da lista")
    print("5. Sair")

minha_lista = []

adicionar = lambda lista, elemento: lista + [elemento]
visualizar = lambda lista, elemento: lista.index(elemento) + 1 if elemento in lista else -1
atualizar = lambda lista, antigo, novo: [novo if item == antigo else item for item in lista]
remover = lambda lista, elemento: [item for item in lista if item != elemento]

while True:
    menu()
    opcao = input("\nDigite o número da opção desejada: ")

    if opcao == '1':
        elemento = input("Digite o elemento a ser adicionado: ")
        minha_lista = adicionar(minha_lista, elemento)
        print(f"Elemento '{elemento}' adicionado à lista.")
    
    elif opcao == '2':
        if not minha_lista:
            print("A lista está vazia.")
            continue
        elemento = input("Digite o elemento a ser visualizado: ")
        posicao = visualizar(minha_lista, elemento)
        if posicao != -1:
            print(f"Elemento '{elemento}' encontrado na posição {posicao}.")
        else:
            print(f"Elemento '{elemento}' não encontrado na lista.")
    
    elif opcao == '3':
        if not minha_lista:
            print("A lista está vazia.")
            continue
        elemento_antigo = input("Digite o elemento a ser atualizado: ")
        elemento_novo = input("Digite o novo elemento: ")

        nova_lista = atualizar(minha_lista, elemento_antigo, elemento_novo)
        if nova_lista != minha_lista:
            minha_lista = nova_lista
            print(f"Elemento '{elemento_antigo}' atualizado para '{elemento_novo}'.")
        else:
            print(f"Elemento '{elemento_antigo}' não encontrado na lista.")
            
    elif opcao == '4':
        if not minha_lista:
            print("A lista está vazia.")
            continue
        elemento = input("Digite o elemento a ser removido: ")
        
        nova_lista = remover(minha_lista, elemento)
        if nova_lista != minha_lista:
            minha_lista = nova_lista
            print(f"Elemento '{elemento}' removido da lista.")
        else:
            print(f"Elemento '{elemento}' não encontrado na lista.")

    elif opcao == '5':
        print("Saindo...")
        time.sleep(0.5)
        break

    else:
        print("Opção inválida. Tente novamente.")
    print(f"\nLista atual: {minha_lista}")