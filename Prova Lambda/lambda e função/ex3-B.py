#com lambda e ordem superior

inteiros = [2, 5, 8, 11, 14, 17] #lista de numeros inteiros

pares = list(filter(lambda x: x % 2 == 0, inteiros)) #lambda dos pares (resumo o "list" transforma em lista e o "filter" filtra os valores que vou usar)
impares = list(filter(lambda x: x % 2 == 1, inteiros)) #lambda dos impares (mesma logica de cima)

print(f"entrada: {inteiros}") #printar inteiro
print(f"pares: {pares}") #printar pares
print(f"impares: {impares}") #printar impares