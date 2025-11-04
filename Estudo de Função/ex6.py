def numero_na_lista(lista, numero):
    return numero in lista

minha_lista = [1, 2, 3, 4, 5]
num = int(input("Digite um numero para verificar se esta na lista: "))
resultado = numero_na_lista(minha_lista, num)
print(f"O numero {num} esta na lista? {resultado}")