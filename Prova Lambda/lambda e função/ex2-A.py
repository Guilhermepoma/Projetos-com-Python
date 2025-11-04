#com DEF

lista_notas = [8, 7, 6, 9] #lista das notas

def media_notas(lista_notas): #definindo a funcao media_notas
    total = sum(lista_notas) / len(lista_notas) #calculando a media das notas (no resumo ela vai somar os valores e dividir pela quantidade de valores)

    if total >= 7: #verificando se a media é maior ou igual a 7
        print(f"sua media é: {total} e voce foi aprovado!") #printando a media e a mensagem de aprovado
    else:
        print(f"sua media é: {total} e voce foi reprovado!") #printando a media e a mensagem de reprovado
media_notas(lista_notas) #chamando a funcao media_notas