#com DEF

inteiros = [2, 5, 8, 11, 14, 17] #lista de numeros inteiros
pares = [] #lista de numeros pares (que vai receber os valores ainda)
impares = [] #lista de numeros impares (que vai receber os valores ainda)

def separar_numeros(lista): #definindo a funcao separar_numeros que vai receber a lista
    for i in lista: #for para percorrer a lista
        if i % 2 == 0: #verificando se o numero é par
            pares.append(i) #se for par, adiciona na lista de pares
        else: #senao
            impares.append(i) #adiciona na lista de impares

    #varios prints         
    print(f"entrada: {inteiros}") #printar inteiro
    print(f"pares: {pares}") #printar pares
    print(f"impares: {impares}") #printar impares

separar_numeros(inteiros) #chamando a funcao separar_numeros com a lista de inteiros