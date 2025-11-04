#com DEF

num_interio = int(input("Digite um numero inteiro: ")) #vai receber um numero inteiro

def calcular(val): #definindo a funcao calcular
    dobro = num_interio * 2 #calculando o dobro
    triplo = num_interio * 3 #calculando o triplo
    raiz = num_interio ** (1/2) #calculando a raiz quadrada

    print(f"O dobro é {dobro}") #printando o dobro
    print(f"O triplo é {triplo}") #printando o triplo
    print(f"A raiz quadrada é {raiz:.2f}") #printando a raiz quadrada com 2 casas decimais

calcular(num_interio) #chamando a funcao calcular com o numero inteiro