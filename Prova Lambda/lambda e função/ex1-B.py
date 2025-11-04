#com lambda

num_interio = int(input("Digite um numero inteiro: ")) #vai receber um numero inteiro

calcular = lambda val: (val * 2, val * 3, val ** (1/2)) #definindo a funcao calcular com lambda
dobro, triplo, raiz = calcular(num_interio) #chamando a funcao calcular com o numero inteiro
print(f"O dobro é {dobro}") #printando o dobro
print(f"O triplo é {triplo}")  #printando o triplo
print(f"A raiz quadrada é {raiz:.2f}") #printando a raiz quadrada com 2 casas decimais