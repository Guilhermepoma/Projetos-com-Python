import tkinter as tk
import time
import pygame  # Biblioteca para reprodução de som

# Inicializa o mixer do pygame
pygame.mixer.init()

# Função para atualizar o relógio em tempo real
def atualizar_tempo():
    local_time = time.localtime()
    formatted_time = time.strftime("%Y-%m-%d %H:%M:%S", local_time)
    label_tempo.config(text=f"Hora Atual: {formatted_time}")
    label_tempo.after(1000, atualizar_tempo)  # Atualiza a cada 1000 ms (1 segundo)

# Função para iniciar o timer
def iniciar_timer():
    try:
        tempo_restante = int(entry_tempo.get())
        contar_regressivamente(tempo_restante)
    except ValueError:
        label_timer.config(text="Insira um número válido!")

# Função para contar regressivamente
def contar_regressivamente(tempo):
    if tempo > 0:
        minutos, segundos = divmod(tempo, 60)
        label_timer.config(text=f"Timer: {minutos:02d}:{segundos:02d}")
        janela.after(1000, contar_regressivamente, tempo - 1)
    else:
        label_timer.config(text="Tempo esgotado!")
        tocar_som()

# Função para tocar som ao final do timer
def tocar_som():
    try:
        pygame.mixer.music.load('som_final.mp3')  # Substitua 'som_final.mp3' pelo caminho do seu arquivo de som
        pygame.mixer.music.play()
    except pygame.error as e:
        print(f"Erro ao reproduzir som: {e}")

# Criação da janela principal
janela = tk.Tk()
janela.title("Relógio e Timer")

# Relógio em tempo real
label_tempo = tk.Label(janela, text="", font=("Arial", 16))
label_tempo.pack(pady=10)
atualizar_tempo()

# Timer
frame_timer = tk.Frame(janela)
frame_timer.pack(pady=10)

label_instrucoes = tk.Label(frame_timer, text="Insira o tempo em segundos:", font=("Arial", 12))
label_instrucoes.pack(side=tk.LEFT, padx=5)

entry_tempo = tk.Entry(frame_timer, width=10, font=("Arial", 12))
entry_tempo.pack(side=tk.LEFT, padx=5)

botao_iniciar = tk.Button(frame_timer, text="Iniciar Timer", font=("Arial", 12), command=iniciar_timer)
botao_iniciar.pack(side=tk.LEFT, padx=5)

label_timer = tk.Label(janela, text="Timer: 00:00", font=("Arial", 16))
label_timer.pack(pady=10)

# Inicia o loop principal da interface gráfica
janela.mainloop()