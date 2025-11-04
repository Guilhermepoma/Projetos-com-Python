def soma_inteiros(n):
    return sum(range(1, n + 1))

n = int(input("Digite um número inteiro positivo: "))
resultado = soma_inteiros(n)
print(f"A soma dos inteiros de 1 a {n} é: {resultado}")