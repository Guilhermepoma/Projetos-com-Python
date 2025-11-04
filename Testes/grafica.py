import tkinter as tk

#função que executado pelo botao
def saudacao():
    nome=entrada_nome.get() #pega o nome digitado
    if nome.strip():
        mensagem.config(text=f"Seja bem-vindo, {nome}!")
    else:
        mensagem.config(text="Por favor, digite seu nome.")


#criação da janela principal
janela = tk.Tk()
janela.title("Gerador de Boas Vindas")
janela.geometry("400x250") #largura x altura

#titulo da aplicação
titulo = tk.Label(janela, text="Interface grafica com python", font=("Arial", 16, "bold"))
titulo.pack(pady=10) #adiciona margem superior

#rotulo explicativo para o usuario
rotulo = tk.Label(janela, text="Digite seu nome abaixo:", font=("Arial", 12))

#entrada de text
entrada_nome = tk.Entry(janela, font=("Arial", 12), justify="center")
entrada_nome.pack(pady=10)

#botao que aciona a saudação
botao = tk.Button(janela, text="Gerar mensagem", font=("Arial", 12, "bold"), bg="#4CAF50", fg="white", command=saudacao)
botao.pack(pady=10)

mensagem = tk.Label(janela, text="", font=("Arial", 12), fg="blue")
mensagem.pack(pady=10)

janela.mainloop()