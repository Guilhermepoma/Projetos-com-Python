def eh_bissexto(ano):
    return (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)

ano = int(input("Digite um ano para verificar se é bissexto: "))
resultado = eh_bissexto(ano)
print(f"O ano {ano} é bissexto? {resultado}")