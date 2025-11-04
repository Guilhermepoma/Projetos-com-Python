import tkinter as tk
from tkinter import messagebox
import random 

def jogador(escolha_jogador):
    opcoes = ['Pedra', 'Papel', 'Tesoura']
    escolha_computador = random.choice(opcoes)
    
    if escolha_jogador == escolha_computador:
        resultado = "Empate!"
    elif (escolha_jogador == 'Pedra' and escolha_computador == 'Tesoura') or \
         (escolha_jogador == 'Papel' and escolha_computador == 'Pedra') or \
         (escolha_jogador == 'Tesoura' and escolha_computador == 'Papel'):
        resultado = "Você venceu!"
    else:
        resultado = "Computador venceu!"
    
    messagebox.showinfo("Resultado", f"Você escolheu: {escolha_jogador}\nComputador escolheu: {escolha_computador}\n{resultado}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Jogo Pedra, Papel e Tesoura")
janela.geometry("300x200")
# Título da aplicação
titulo = tk.Label(janela, text="Pedra, Papel e Tesoura", font=("Arial", 16, "bold"))
titulo.pack(pady=10)
# Botões para as escolhas
botao_pedra = tk.Button(janela, text="Pedra", font=("Arial", 12), command=lambda: jogador('Pedra'))
botao_pedra.pack(pady=5)
botao_papel = tk.Button(janela, text="Papel", font=("Arial", 12), command=lambda: jogador('Papel'))
botao_papel.pack(pady=5)
botao_tesoura = tk.Button(janela, text="Tesoura", font=("Arial", 12), command=lambda: jogador('Tesoura'))
botao_tesoura.pack(pady=5)
janela.mainloop()