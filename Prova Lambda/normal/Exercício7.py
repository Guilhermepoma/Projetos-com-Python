import random

def jogar():
    """ Jogo de adivinhação de número entre 1 e 100."""
    numero_secreto = random.randint(1, 100)
    while True:
        chute = int(input("Digite um número entre 1 e 100: "))
        if chute < 1 or chute > 100:
            print("Número inválido! Tente novamente.")
            continue
        elif chute == numero_secreto:
            print("Parabéns! Você acertou!")
            break
        elif chute != numero_secreto:
            print("Você errou! Tente novamente.")

jogar()