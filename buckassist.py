import tkinter as tk
from tkinter import ttk, messagebox
from tkinter.font import Font

class JogoBolasApp:
    def __init__(self, root):
        # Configuração da janela principal
        self.root = root
        self.root.title("Buckshot Assistant")
        self.root.geometry("550x700")  # Tamanho maior para o histórico
        self.root.resizable(True, True)
        
        # Configuração de cores para modo escuro
        self.bg_color = "#1a1a1a"       # Fundo principal (cinza muito escuro)
        self.frame_color = "#2d2d2d"     # Fundo dos painéis
        self.text_color = "#ffffff"      # Texto branco
        self.accent_blue = "#3498db"     # Azul para bolas azuis
        self.accent_red = "#e74c3c"      # Vermelho para bolas vermelhas
        self.accent_green = "#2ecc71"    # Verde para acertos
        self.accent_yellow = "#f1c40f"   # Amarelo para informações
        self.disabled_color = "#7f8c8d"  # Cinza para elementos desativados
        
        # Configuração do tema Clam
        self.style = ttk.Style()
        self.style.theme_use('clam')
        
        # Personalização do tema Clam para modo escuro
        self.style.configure('.', background=self.frame_color,
                           foreground=self.text_color,
                           fieldbackground=self.frame_color,
                           selectbackground=self.accent_blue,
                           selectforeground=self.text_color)
        
        self.style.configure('TFrame', background=self.frame_color)
        self.style.configure('TLabel', background=self.frame_color, foreground=self.text_color)
        self.style.configure('TButton', 
                           background="#34495e",
                           foreground=self.text_color,
                           bordercolor="#4a6baf",
                           focusthickness=3,
                           focuscolor='none',
                           font=('Helvetica', 10, 'bold'),
                           padding=6)
        
        self.style.map('TButton',
                      background=[('active', '#2c3e50'), ('disabled', self.disabled_color)],
                      foreground=[('disabled', self.text_color)])
        
        self.style.configure('TEntry', 
                           fieldbackground="#3d3d3d",
                           foreground=self.text_color,
                           insertbackground=self.accent_blue,
                           bordercolor="#4a6baf",
                           lightcolor="#4a6baf",
                           padding=5)
        
        self.style.configure('TLabelframe', 
                           background=self.frame_color,
                           bordercolor="#4a6baf",
                           relief=tk.GROOVE,
                           labelmargins=10)
        
        self.style.configure('TLabelframe.Label', 
                           background=self.frame_color,
                           foreground=self.accent_blue,
                           font=('Helvetica', 10, 'bold'))
        
        self.style.configure('Vertical.TScrollbar',
                           background="#3d3d3d",
                           troughcolor=self.frame_color,
                           bordercolor=self.frame_color,
                           arrowcolor=self.text_color)
        
        # Configurar o fundo principal
        self.root.configure(bg=self.bg_color)
        
        # Variáveis de controle
        self.A_inicial = tk.IntVar(value=0)
        self.V_inicial = tk.IntVar(value=0)
        self.A_restante = 0
        self.V_restante = 0
        self.previsoes_corretas = 0
        self.total_retiradas = 0
        self.historico = []
        self.previsao_usuario = tk.StringVar()
        
        # Container principal
        self.main_frame = ttk.Frame(root, padding="15")
        self.main_frame.pack(fill=tk.BOTH, expand=True)
        
        # Seção de configuração
        self.config_frame = ttk.LabelFrame(self.main_frame, text=" CONFIGURAÇÃO INICIAL ", padding=(15, 10))
        self.config_frame.pack(fill=tk.X, pady=(0, 15))
        
        # Entradas de dados
        ttk.Label(self.config_frame, text="Bolas Azuis:").grid(row=0, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_azul = ttk.Entry(self.config_frame, textvariable=self.A_inicial)
        self.entry_azul.grid(row=0, column=1, padx=5, pady=5, sticky=tk.EW)
        
        ttk.Label(self.config_frame, text="Bolas Vermelhas:").grid(row=1, column=0, sticky=tk.W, padx=5, pady=5)
        self.entry_vermelho = ttk.Entry(self.config_frame, textvariable=self.V_inicial)
        self.entry_vermelho.grid(row=1, column=1, padx=5, pady=5, sticky=tk.EW)
        
        self.btn_iniciar = ttk.Button(self.config_frame, text="INICIAR JOGO", command=self.iniciar_jogo)
        self.btn_iniciar.grid(row=2, column=0, columnspan=2, pady=(10, 5), sticky=tk.EW)
        
        # Seção de status
        self.status_frame = ttk.LabelFrame(self.main_frame, text=" STATUS DA URNA ", padding=(15, 10))
        self.status_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.label_status = ttk.Label(self.status_frame, text="Aguardando início...", font=('Helvetica', 11, 'bold'))
        self.label_status.pack()
        
        # Barra de probabilidade
        self.prob_frame = ttk.LabelFrame(self.main_frame, text=" PROBABILIDADES ", padding=(15, 10))
        self.prob_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.canvas = tk.Canvas(self.prob_frame, height=20, bg='#3d3d3d', highlightthickness=0)
        self.canvas.pack(fill=tk.X)
        
        self.prob_labels = ttk.Frame(self.prob_frame)
        self.prob_labels.pack(fill=tk.X, pady=(5, 0))
        
        self.label_azul = ttk.Label(self.prob_labels, text="Azul: 0%", foreground=self.accent_blue, font=('Helvetica', 9, 'bold'))
        self.label_azul.pack(side=tk.LEFT, expand=True)
        
        self.label_vermelho = ttk.Label(self.prob_labels, text="Vermelho: 0%", foreground=self.accent_red, font=('Helvetica', 9, 'bold'))
        self.label_vermelho.pack(side=tk.RIGHT, expand=True)
        
        # Previsão automática
        self.prediction_frame = ttk.LabelFrame(self.main_frame, text=" PREVISÃO AUTOMÁTICA ", padding=(15, 10))
        self.prediction_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.prediction_label = ttk.Label(self.prediction_frame, text="Nenhuma previsão disponível", 
                                        font=('Helvetica', 11), foreground=self.accent_yellow)
        self.prediction_label.pack()
        
        # Controles do jogo
        self.controls_frame = ttk.Frame(self.main_frame)
        self.controls_frame.pack(fill=tk.X, pady=(0, 15))
        
        self.btn_retirar_azul = ttk.Button(self.controls_frame, text="RETIRAR AZUL", 
                                          command=lambda: self.retirar_bala('a'), state=tk.DISABLED)
        self.btn_retirar_azul.pack(side=tk.LEFT, expand=True, padx=5)
        
        self.btn_retirar_vermelha = ttk.Button(self.controls_frame, text="RETIRAR VERMELHA", 
                                              command=lambda: self.retirar_bala('v'), state=tk.DISABLED)
        self.btn_retirar_vermelha.pack(side=tk.RIGHT, expand=True, padx=5)
        
        # Histórico
        self.history_frame = ttk.LabelFrame(self.main_frame, text=" HISTÓRICO ", padding=(15, 10))
        self.history_frame.pack(fill=tk.BOTH, expand=True)
        
        self.historico_text = tk.Text(self.history_frame, height=12, state=tk.DISABLED, 
                                     bg="#3d3d3d", fg=self.text_color, font=('Consolas', 9), 
                                     padx=10, pady=10, wrap=tk.WORD, insertbackground=self.accent_blue,
                                     selectbackground=self.accent_blue, selectforeground="#000000")
        self.historico_text.pack(fill=tk.BOTH, expand=True)
        
        # Barra de rolagem
        scrollbar = ttk.Scrollbar(self.historico_text)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
        self.historico_text.config(yscrollcommand=scrollbar.set)
        scrollbar.config(command=self.historico_text.yview)

    def iniciar_jogo(self):
        try:
            self.A_restante = self.A_inicial.get()
            self.V_restante = self.V_inicial.get()
            
            if self.A_restante < 0 or self.V_restante < 0:
                messagebox.showerror("Erro", "Os valores não podem ser negativos")
                return
                
            self.previsoes_corretas = 0
            self.total_retiradas = 0
            self.historico = []
            self.atualizar_interface()

            self.historico_text.config(state=tk.NORMAL)
            self.historico_text.delete("1.0", tk.END)
            self.historico_text.insert(tk.END, "Jogo iniciado!\n", "info")
            self.historico_text.tag_config("info", foreground=self.accent_blue)
            self.historico_text.config(state=tk.DISABLED)

            self.btn_retirar_azul.config(state=tk.NORMAL if self.A_restante > 0 else tk.DISABLED)
            self.btn_retirar_vermelha.config(state=tk.NORMAL if self.V_restante > 0 else tk.DISABLED)
            
        except tk.TclError:
            messagebox.showerror("Erro", "Por favor, insira valores numéricos válidos")

    def atualizar_interface(self):
        total_restante = self.A_restante + self.V_restante
        
        if total_restante > 0:
            prob_azul = (self.A_restante / total_restante * 100)
            prob_vermelha = (self.V_restante / total_restante * 100)
        else:
            prob_azul = prob_vermelha = 0
            
        # Atualiza status
        status_text = f"Urna: {self.A_restante} Azuis, {self.V_restante} Vermelhas"
        if total_restante == 0:
            status_text += " (Vazia)"
        self.label_status.config(text=status_text)
        
        # Atualiza barra de probabilidade
        self.canvas.delete("all")
        width = self.canvas.winfo_width()
        
        azul_width = width * (prob_azul / 100)
        self.canvas.create_rectangle(0, 0, azul_width, 20, fill=self.accent_blue, outline="")
        self.canvas.create_rectangle(azul_width, 0, width, 20, fill=self.accent_red, outline="")
        
        # Atualiza labels de probabilidade
        self.label_azul.config(text=f"Azul: {prob_azul:.1f}%")
        self.label_vermelho.config(text=f"Vermelho: {prob_vermelha:.1f}%")
        
        # Atualiza previsão
        if total_restante > 0:
            previsao = 'a' if prob_azul >= prob_vermelha else 'v'
            self.previsao_usuario.set(previsao)
            
            cor = self.accent_blue if previsao == 'a' else self.accent_red
            texto = "Azul" if previsao == 'a' else "Vermelha"
            self.prediction_label.config(text=f"Previsão: {texto}", foreground=cor)
        else:
            self.prediction_label.config(text="Urna vazia", foreground=self.disabled_color)
        
        # Atualiza estado dos botões
        self.btn_retirar_azul.config(state=tk.NORMAL if self.A_restante > 0 else tk.DISABLED)
        self.btn_retirar_vermelha.config(state=tk.NORMAL if self.V_restante > 0 else tk.DISABLED)

    def retirar_bala(self, cor):
        if cor == 'a' and self.A_restante > 0:
            self.A_restante -= 1
        elif cor == 'v' and self.V_restante > 0:
            self.V_restante -= 1
        else:
            return

        self.total_retiradas += 1
        previsao = self.previsao_usuario.get()
        acertou = previsao == cor
        
        if acertou:
            self.previsoes_corretas += 1

        # Formatação do histórico
        cor_texto = "Azul" if cor == 'a' else "Vermelha"
        previsao_texto = "Azul" if previsao == 'a' else "Vermelha"
        resultado = "✓ Acertou" if acertou else "✗ Errou"
        cor_resultado = self.accent_green if acertou else self.accent_red
        
        entry = f"Retirada: {cor_texto:<10} | Previsão: {previsao_texto:<10} | {resultado}"
        self.historico.append(entry)

        self.historico_text.config(state=tk.NORMAL)
        self.historico_text.insert(tk.END, entry + "\n", resultado)
        self.historico_text.tag_config(resultado, foreground=cor_resultado)
        self.historico_text.see(tk.END)
        self.historico_text.config(state=tk.DISABLED)

        self.atualizar_interface()

        if self.A_restante + self.V_restante == 0:
            precisao = (self.previsoes_corretas / self.total_retiradas * 100) if self.total_retiradas > 0 else 0
            messagebox.showinfo("Fim de Jogo", 
                              f"A urna está vazia!\n\nPrecisão das previsões: {precisao:.1f}%\n"
                              f"Acertos: {self.previsoes_corretas}/{self.total_retiradas}")

if __name__ == "__main__":
    root = tk.Tk()
    
    # Configuração para tornar a interface mais nítida em monitores HD
    try:
        from ctypes import windll
        windll.shcore.SetProcessDpiAwareness(1)
    except:
        pass
        
    app = JogoBolasApp(root)
    root.mainloop()