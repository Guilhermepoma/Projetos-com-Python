import time

def cadastrar_nota(notas, aluno, nota):
    """Cadastra a nota de um aluno na lista de notas."""
    notas[aluno] = nota
    if nota < 0 or nota > 10:
        print("Aviso: A nota deve estar entre 0 e 10.")
    print(f"Nota {nota} cadastrada para o aluno '{aluno}'.")

def alterar_nota(notas, aluno, nova_nota):
    """Altera a nota de um aluno existente na lista de notas."""
    if aluno in notas:
        notas[aluno] = nova_nota
        print(f"Nota do aluno '{aluno}' alterada para {nova_nota}.")
    else:
        print(f"Aluno '{aluno}' não encontrado.")

def excluir_nota(notas, aluno):
    """Exclui a nota de um aluno da lista de notas."""
    if aluno in notas:
        del notas[aluno]
        print(f"Nota do aluno '{aluno}' removida.")

def exibir_nota(notas, aluno):
    """Exibe a nota de um aluno da lista de notas."""
    if aluno in notas:
        print(f"A nota do aluno '{aluno}' é {notas[aluno]}.")
    else:
        print(f"Aluno '{aluno}' não encontrado.")

def calcular_media_turma(notas):
    """Calcula e exibe a média das notas da turma."""
    if notas:
        media = sum(notas.values()) / len(notas)
        print(f"A média da turma é {media:.2f}.")
    else:
        print("Nenhuma nota cadastrada.")

def menu():
    """Exibe o menu de opções para o usuário."""
    print("\nEscolha uma opção:")
    print("1. Cadastrar nota")
    print("2. Alterar nota")
    print("3. Excluir nota")
    print("4. Exibir nota")
    print("5. Calcular média da turma")
    print("6. Sair")

notas = {}

while True:
    menu()
    opcao = input("\nDigite o número da opção desejada: ")
    if opcao == '1':
        aluno = input("Digite o nome do aluno: ")
        nota = float(input("Digite a nota do aluno: "))
        cadastrar_nota(notas, aluno, nota)
    elif opcao == '2':
        aluno = input("Digite o nome do aluno cuja nota será alterada: ")
        nova_nota = float(input("Digite a nova nota do aluno: "))
        alterar_nota(notas, aluno, nova_nota)
    elif opcao == '3':
        aluno = input("Digite o nome do aluno cuja nota será excluída: ")
        excluir_nota(notas, aluno)
    elif opcao == '4':
        aluno = input("Digite o nome do aluno cuja nota será exibida: ")
        exibir_nota(notas, aluno)
    elif opcao == '5':
        calcular_media_turma(notas)
    elif opcao == '6':
        print("Saindo...")
        time.sleep(1)
        break
    else:
        print("Opção inválida. Tente novamente.")
