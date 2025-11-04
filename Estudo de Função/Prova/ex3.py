saldo = 1000 #defini o saldo atual
limite = 500 #defini o limite

valor = int(input("Digite o valor a ser sacado: "))

def sacar(valor): #criei uma função chamada sacar que usara como base o valor para os calculos
    global saldo #isso funciona para eu puxar variaveis de fora da função, sem ele o meu codigo não funciona :)
    if valor <= saldo and valor <= limite: #fiz um if para verificar se o limite é maior ou igual a o saldo e o limite
        saldo -= valor # se sim ele tira o valor do saldo
        print(f"saque realizado. saldo atual: {saldo}") #e mostra-ra o saldo
    else: # senão
        print("saque não autorizado") #ele não autoriza
    
    #outro if
    if valor <= 500: #se o valor for menor ou igual a 500
        print("True") #ele printara TRUE
    else: #senao
        print("False") #ele printara False

sacar(valor) #aqui ele ira chamar a função, e entao mostra-ra com base no "valor"