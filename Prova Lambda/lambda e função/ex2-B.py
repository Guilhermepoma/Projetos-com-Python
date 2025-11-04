#com lambda e ordem superior

lista_notas = [8, 7, 6, 9] #lista das notas

media_notas = lambda notas: sum(notas) / len(notas) #definindo a lambda media_notas (no resumo ela vai somar os valores e dividir pela quantidade de valores)
total = media_notas(lista_notas) #vai chamar a lambda media_notas com a lista de notas

if total >= 7: #verificando se a media é maior ou igual a 7
    print(f"sua media é: {total} e voce foi aprovado!") #printando a media e a mensagem de aprovado
else: #senao
    print(f"sua media é: {total} e voce foi reprovado!") #printando a media e a mensagem de reprovado