import tkinter as tk
from tkinter import ttk, messagebox
import random
import time
import threading

class RoletaGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("🎰 Roleta Tripla 🎰")
        self.root.geometry("440x800")
        self.root.configure(bg='#2C3E50')
        
        # Configuração do jogo
        self.saldo = 100.0
        self.aposta_minima = 5
        self.aposta_maxima = 50
        self.aposta_atual = 0
        self.rodando = False
        self.modo_trapaca = False
        
        self.criar_interface()
        self.atualizar_display()
    
    def criar_interface(self):
        # Frame principal
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
        
        # Título
        titulo = tk.Label(main_frame, text="🎰 ROLETA TRIPLA 🎰", 
                         font=('Arial', 20, 'bold'), 
                         fg='#E74C3C', bg='#2C3E50')
        titulo.grid(row=0, column=0, columnspan=3, pady=(0, 20))
        
        # Display do saldo
        self.saldo_label = tk.Label(main_frame, text="", 
                                   font=('Arial', 16, 'bold'),
                                   fg='#27AE60', bg='#2C3E50')
        self.saldo_label.grid(row=1, column=0, columnspan=3, pady=(0, 10))
        
        # Frame dos números da roleta
        numeros_frame = ttk.LabelFrame(main_frame, text="Roleta", padding="15")
        numeros_frame.grid(row=2, column=0, columnspan=3, pady=20, sticky=(tk.W, tk.E))
        
        # Display dos números
        self.numero_labels = []
        for i in range(3):
            label = tk.Label(numeros_frame, text="?", 
                           font=('Arial', 30, 'bold'), 
                           width=4, height=2,
                           bg='#34495E', fg='#ECF0F1',
                           relief='raised', bd=3)
            label.grid(row=0, column=i, padx=10)
            self.numero_labels.append(label)
        
        # Frame de aposta
        aposta_frame = ttk.LabelFrame(main_frame, text="Fazer Aposta", padding="15")
        aposta_frame.grid(row=3, column=0, columnspan=3, pady=20, sticky=(tk.W, tk.E))
        
        # Entrada de aposta
        tk.Label(aposta_frame, text="Valor da Aposta:", 
                font=('Arial', 12)).grid(row=0, column=0, sticky=tk.W)
        
        self.aposta_entry = ttk.Entry(aposta_frame, font=('Arial', 12), width=10)
        self.aposta_entry.grid(row=0, column=1, padx=10)
        self.aposta_entry.insert(0, "10")
        
        # Botões de aposta rápida
        botoes_frame = ttk.Frame(aposta_frame)
        botoes_frame.grid(row=1, column=0, columnspan=2, pady=10)
        
        valores_aposta = [5, 10, 20, 50]
        for i, valor in enumerate(valores_aposta):
            btn = ttk.Button(botoes_frame, text=f"R$ {valor}",
                           command=lambda v=valor: self.definir_aposta(v))
            btn.grid(row=0, column=i, padx=5)
        
        # Botões de controle
        botoes_controle_frame = ttk.Frame(main_frame)
        botoes_controle_frame.grid(row=4, column=0, columnspan=3, pady=20)
        
        self.girar_btn = ttk.Button(botoes_controle_frame, text="🎯 GIRAR ROLETA",
                                   command=self.iniciar_giro,
                                   style='Accent.TButton')
        self.girar_btn.grid(row=0, column=0, padx=10)
        
        ttk.Button(botoes_controle_frame, text="🔄 REINICIAR JOGO",
                  command=self.reiniciar_jogo).grid(row=0, column=1, padx=10)
        
        ttk.Button(botoes_controle_frame, text="📖 REGRAS",
                  command=self.mostrar_regras).grid(row=0, column=2, padx=10)
        
        # Display de resultado
        self.resultado_label = tk.Label(main_frame, text="", 
                                       font=('Arial', 14, 'bold'),
                                       bg='#2C3E50')
        self.resultado_label.grid(row=5, column=0, columnspan=3, pady=10)
        
        # Histórico
        historico_frame = ttk.LabelFrame(main_frame, text="Histórico", padding="10")
        historico_frame.grid(row=6, column=0, columnspan=3, pady=10, sticky=(tk.W, tk.E))
        
        self.historico_text = tk.Text(historico_frame, height=4, width=50,
                                     font=('Arial', 10), state=tk.DISABLED)
        self.historico_text.grid(row=0, column=0, sticky=(tk.W, tk.E))
        
        scrollbar = ttk.Scrollbar(historico_frame, orient=tk.VERTICAL, 
                                 command=self.historico_text.yview)
        scrollbar.grid(row=0, column=1, sticky=(tk.N, tk.S))
        self.historico_text.configure(yscrollcommand=scrollbar.set)
        
        # 🔥 BOTÃO ESCONDIDO - SEMPRE GANHA 🔥
        self.criar_botao_escondido(main_frame)
        
        # Indicador de modo trapaça (invisível inicialmente)
        self.trapaca_label = tk.Label(main_frame, text="", 
                                     font=('Arial', 10, 'italic'),
                                     bg='#2C3E50', fg='#F39C12')
        self.trapaca_label.grid(row=8, column=0, columnspan=3, pady=5)
    
    def criar_botao_escondido(self, parent):
        """Cria o botão escondido de sempre ganhar"""
        # Frame invisível para esconder o botão
        frame_escondido = ttk.Frame(parent)
        frame_escondido.grid(row=7, column=0, columnspan=3, pady=5)
        
        # Botão com texto enganoso
        self.botao_trapaca = ttk.Button(frame_escondido, 
                                      text="🔧 Configurações Avançadas",
                                      command=self.alternar_modo_trapaca)
        self.botao_trapaca.grid(row=0, column=0)
        
        # Botão de ativação por clique secreto no título
        titulo_bind = parent.grid_slaves(row=0, column=0)[0]
        titulo_bind.bind("<Button-3>", self.ativar_modo_secreto)  # Clique direito
        titulo_bind.bind("<Double-Button-1>", self.ativar_modo_secreto)  # Duplo clique
        
        # Atalho de teclado secreto
        self.root.bind("<Control-Shift-g>", self.ativar_modo_secreto)  # Ctrl+Shift+G
        self.root.bind("<Control-Shift-G>", self.ativar_modo_secreto)  # Ctrl+Shift+G
    
    def alternar_modo_trapaca(self):
        """Alterna entre modo normal e modo trapaça"""
        self.modo_trapaca = not self.modo_trapaca
        
        if self.modo_trapaca:
            self.trapaca_label.config(text="🎯 MODO GARANTIDO ATIVADO - Você sempre ganhará!")
            messagebox.showinfo("Modo Especial Ativado", 
                              "🔓 Modo Garantido ativado!\n\n"
                              "Agora você sempre ganhará na roleta!\n"
                              "Use com moderação! 😉")
            
            # Mudar aparência do botão
            self.botao_trapaca.config(text="✅ Modo Garantido (ATIVO)")
        else:
            self.trapaca_label.config(text="")
            messagebox.showinfo("Modo Especial Desativado", 
                              "Modo Garantido desativado.\n"
                              "Voltando ao modo normal de jogo.")
            
            # Voltar aparência normal do botão
            self.botao_trapaca.config(text="🔧 Configurações Avançadas")
    
    def ativar_modo_secreto(self, event=None):
        """Ativa o modo secreto através de métodos alternativos"""
        if not self.modo_trapaca:
            self.modo_trapaca = True
            self.trapaca_label.config(text="🎯 MODO GARANTIDO ATIVADO - Você sempre ganhará!")
            
            # Mostrar mensagem secreta
            messagebox.showinfo("Easter Egg Ativado!", 
                              "🎉 Parabéns! Você descobriu o segredo!\n\n"
                              "Modo Garantido ativado via Easter Egg!\n"
                              "Agora você sempre ganhará! 🍀")
            
            self.botao_trapaca.config(text="✅ Modo Garantido (ATIVO)")
    
    def definir_aposta(self, valor):
        """Define o valor da aposta"""
        self.aposta_entry.delete(0, tk.END)
        self.aposta_entry.insert(0, str(valor))
    
    def obter_aposta(self):
        """Obtém e valida a aposta"""
        try:
            aposta = float(self.aposta_entry.get())
            if aposta < self.aposta_minima:
                messagebox.showwarning("Aposta Baixa", 
                                     f"Aposta mínima: R$ {self.aposta_minima}")
                return None
            if aposta > self.aposta_maxima:
                messagebox.showwarning("Aposta Alta", 
                                     f"Aposta máxima: R$ {self.aposta_maxima}")
                return None
            if aposta > self.saldo:
                messagebox.showerror("Saldo Insuficiente", 
                                   "Você não tem saldo suficiente!")
                return None
            return aposta
        except ValueError:
            messagebox.showerror("Erro", "Digite um valor numérico válido!")
            return None
    
    def iniciar_giro(self):
        """Inicia o giro da roleta em uma thread separada"""
        if self.rodando:
            return
        
        aposta = self.obter_aposta()
        if aposta is None:
            return
        
        self.aposta_atual = aposta
        self.rodando = True
        self.girar_btn.config(state='disabled')
        self.resultado_label.config(text="Girando...", fg='#F39C12')
        
        # Executar o giro em thread separada para não travar a interface
        threading.Thread(target=self.executar_giro, daemon=True).start()
    
    def executar_giro(self):
        """Executa a animação do giro e calcula o resultado"""
        # Animação do giro
        for _ in range(10):
            if not self.rodando:
                break
            if self.modo_trapaca:
                # No modo trapaça, mostrar números iguais durante a animação
                numero_trapaca = random.randint(0, 9)
                numeros_temp = [numero_trapaca, numero_trapaca, numero_trapaca]
            else:
                numeros_temp = [random.randint(0, 9) for _ in range(3)]
            
            self.atualizar_numeros(numeros_temp)
            time.sleep(0.1)
        
        # Resultado final
        if self.modo_trapaca:
            # Sempre ganha no modo trapaça
            numero_vencedor = random.randint(0, 9)
            numeros_finais = [numero_vencedor, numero_vencedor, numero_vencedor]
        else:
            # Modo normal
            numeros_finais = [random.randint(0, 9) for _ in range(3)]
        
        self.atualizar_numeros(numeros_finais)
        
        # Calcular resultado
        self.processar_resultado(numeros_finais)
        
        self.rodando = False
        self.root.after(0, self.finalizar_giro)
    
    def atualizar_numeros(self, numeros):
        """Atualiza os números na interface (deve ser chamado na thread principal)"""
        def atualizar():
            for i, numero in enumerate(numeros):
                self.numero_labels[i].config(text=str(numero))
        
        self.root.after(0, atualizar)
    
    def processar_resultado(self, numeros):
        """Processa o resultado do giro"""
        vitoria = len(set(numeros)) == 1
        
        if vitoria:
            premio = self.aposta_atual * 10
            self.saldo += premio
            if self.modo_trapaca:
                mensagem = f"🎉 VITÓRIA GARANTIDA! +R$ {premio:.2f}"
            else:
                mensagem = f"🎉 JACKPOT! +R$ {premio:.2f}"
            cor = '#27AE60'
        else:
            self.saldo -= self.aposta_atual
            mensagem = f"💸 Perdeu: -R$ {self.aposta_atual:.2f}"
            cor = '#E74C3C'
        
        # Atualizar interface
        def mostrar_resultado():
            self.resultado_label.config(text=mensagem, fg=cor)
            self.atualizar_display()
            self.adicionar_historico(numeros, vitoria, self.aposta_atual)
        
        self.root.after(0, mostrar_resultado)
    
    def finalizar_giro(self):
        """Finaliza o giro e reabilita controles"""
        self.girar_btn.config(state='normal')
        
        if self.saldo < self.aposta_minima and not self.modo_trapaca:
            messagebox.showinfo("Fim de Jogo", 
                              "Saldo insuficiente para continuar jogando!")
            self.girar_btn.config(state='disabled')
    
    def adicionar_historico(self, numeros, vitoria, aposta):
        """Adiciona resultado ao histórico"""
        self.historico_text.config(state=tk.NORMAL)
        
        if self.historico_text.get(1.0, tk.END).count('\n') > 10:
            self.historico_text.delete(1.0, 2.0)
        
        resultado = "GANHOU" if vitoria else "PERDEU"
        cor = "green" if vitoria else "red"
        
        # Adicionar indicador de trapaça no histórico
        if self.modo_trapaca and vitoria:
            resultado = "GANHOU 🎯"
        
        texto = f"{numeros[0]} | {numeros[1]} | {numeros[2]} - {resultado} - R$ {aposta:.2f}\n"
        
        self.historico_text.insert(tk.END, texto)
        self.historico_text.see(tk.END)
        self.historico_text.config(state=tk.DISABLED)
    
    def atualizar_display(self):
        """Atualiza o display do saldo"""
        self.saldo_label.config(text=f"Saldo: R$ {self.saldo:.2f}")
        
        # Mudar cor do saldo baseado no valor
        if self.saldo < 20:
            cor = '#E74C3C'  # Vermelho
        elif self.saldo < 50:
            cor = '#F39C12'  # Laranja
        else:
            cor = '#27AE60'  # Verde
        
        self.saldo_label.config(fg=cor)
    
    def reiniciar_jogo(self):
        """Reinicia o jogo"""
        self.saldo = 100.0
        self.rodando = False
        self.modo_trapaca = False  # Resetar modo trapaça
        self.girar_btn.config(state='normal')
        self.resultado_label.config(text="")
        self.trapaca_label.config(text="")
        
        for label in self.numero_labels:
            label.config(text="?")
        
        self.botao_trapaca.config(text="🔧 Configurações Avançadas")
        
        self.historico_text.config(state=tk.NORMAL)
        self.historico_text.delete(1.0, tk.END)
        self.historico_text.config(state=tk.DISABLED)
        
        self.atualizar_display()
        messagebox.showinfo("Jogo Reiniciado", "Saldo resetado para R$ 100,00!")
    
    def mostrar_regras(self):
        """Mostra as regras do jogo"""
        regras = """
🎰 REGRAS DA ROLETA TRIPLA 🎰

• Aposte um valor entre R$ 5,00 e R$ 50,00
• A roleta gera 3 números aleatórios (0-9)
• Se TODOS os 3 números forem IGUAIS: 
  🎉 VOCÊ GANHA 10x O VALOR DA APOSTA!
• Caso contrário: você perde a aposta

💡 DICA: A chance de ganhar é de 1 em 1000!

🎯 SEGREDOS:
• Clique duplo ou botão direito no título
• Ou pressione Ctrl+Shift+G
• Ou use o botão "Configurações Avançadas"
        """
        messagebox.showinfo("Regras do Jogo", regras)

def main():
    # Configurar estilo
    root = tk.Tk()
    
    # Tentar usar tema moderno se disponível
    try:
        from ttkthemes import ThemedTk
        root = ThemedTk(theme="arc")
    except ImportError:
        pass
    
    app = RoletaGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()