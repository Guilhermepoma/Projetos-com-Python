def soma_maior(a, b, limite):
    return (a + b) > limite

n1 = int(input("Digite o primeiro numero: "))
n2 = int(input("Digite o segundo numero: "))
limite = int(input("Digite o limite: "))
resultado = soma_maior(n1, n2, limite)
print(f"A soma de {n1} e {n2} é maior que {limite}? {resultado}")