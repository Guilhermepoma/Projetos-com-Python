import math

while True:
    print("Qual voce quer?")
    print("1 - Area do circulo\n2 - Area do retangulo\n3 - Area do triangulo\n4 - Sair")
    esc = int(input("Escolha: "))

    if esc == 1:
        raio = float(input("Digite o raio do circulo: "))
        a_circulo = lambda r: math.pi * (r ** 2)
        resu = a_circulo(raio)
        print(resu)
    
    elif esc == 2:
        base = float(input("Digite o base: "))
        altura = float(input("Digite o altura: "))
        a_retangulo = lambda b,h: b * h
        resu = a_retangulo(base, altura)
        print(resu)

    elif esc == 3:
        base = float(input("Digite o base: "))
        altura = float(input("Digite o altura: "))
        a_retangulo = lambda b,h: (b * h) /2
        resu = a_retangulo(base, altura)
        print(resu)

    elif esc == 4:
        break