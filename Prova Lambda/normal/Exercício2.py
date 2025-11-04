import time

def adicionar_a_lista(lista, elemento):
    """Adiciona um elemento ao final da lista."""
    lista.append(elemento)

def visualizar_da_lista(lista, elemento):
    """Verifica se um elemento está na lista e retorna sua posição (começando do índice 1)."""
    if elemento in lista:
        return lista.index(elemento) + 1
    else:
        return -1
    
def atualizar_na_lista(lista, elemento_antigo, elemento_novo):
    """Atualiza um elemento na lista, substituindo-o por um novo."""
    if elemento_antigo in lista:
        index = lista.index(elemento_antigo)
        lista[index] = elemento_novo
        return True
    else:
        return False
    
def remover_da_lista(lista, elemento):
    """Remove um elemento da lista, se existir."""
    if elemento in lista:
        lista.remove(elemento)
        return True
    else:
        return False
    
def menu():
    """Exibe o menu de opções para o usuário."""
    print("\nEscolha uma opção:")
    print("1. Adicionar um elemento à lista")
    print("2. Visualizar a posição de um elemento na lista")
    print("3. Atualizar um elemento na lista")
    print("4. Remover um elemento da lista")
    print("5. Sair")

minha_lista = []

while True:
    menu()
    opcao = input("\nDigite o número da opção desejada: ")
    if opcao == '1':
        elemento = input("Digite o elemento a ser adicionado: ")
        adicionar_a_lista(minha_lista, elemento)
        print(f"Elemento '{elemento}' adicionado à lista.")
    elif opcao == '2':
        elemento = input("Digite o elemento a ser visualizado: ")
        posicao = visualizar_da_lista(minha_lista, elemento)
        if posicao != -1:
            print(f"Elemento '{elemento}' encontrado na posição {posicao}.")
        else:
            print(f"Elemento '{elemento}' não encontrado na lista.")
    elif opcao == '3':
        elemento_antigo = input("Digite o elemento a ser atualizado: ")
        elemento_novo = input("Digite o novo elemento: ")
        if atualizar_na_lista(minha_lista, elemento_antigo, elemento_novo):
            print(f"Elemento '{elemento_antigo}' atualizado para '{elemento_novo}'.")
        else:
            print(f"Elemento '{elemento_antigo}' não encontrado na lista.")
    elif opcao == '4':
        elemento = input("Digite o elemento a ser removido: ")
        if remover_da_lista(minha_lista, elemento):
            print(f"Elemento '{elemento}' removido da lista.")
        else:
            print(f"Elemento '{elemento}' não encontrado na lista.")
    elif opcao == '5':
        print("Saindo...")
        time.sleep(1)
        break
    else:
        print("Opção inválida. Tente novamente.")