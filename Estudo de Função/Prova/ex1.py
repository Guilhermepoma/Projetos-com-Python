num1 = int(input("Digite o primeiro valor: ")) #vou pedir o 1° valor
num2 = int(input("Digite o segundo valor: ")) #vou pedir o 2° valor
num3 = int(input("Digite o terceiro valor: ")) #vou pedir o 3° valor

def soma(): #criei uma função chamada soma
    if num1 <= num2 <= num3: #fiz um if para verificar se os numeros estão em ordem
        print("True") #se estiverem eu dou um True
    else: #senao
        print("False") #eu dou um False
soma() #aqui ele ira chamar a função, e entao printa-ra (nn sei se escrevi certo)