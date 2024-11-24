import tkinter as tk
import functions

class Interface:
    def __init__(self, raiz):
        self.raiz = raiz
        self.raiz.title("Sudoku")
        self.raiz.configure(background="#d0d0d0")

        self.tamanho_sudoku = 9
        self.entradas = []
        self.sudoku = []
        self.ja_resolvido = False

        painel_principal = tk.Frame(raiz, background="#d4d4d4")
        painel_principal.pack(pady=10)

        self.painel_grade = tk.Frame(raiz)
        self.painel_grade.pack(pady=10)

        self.tamanho_label = tk.Label(painel_principal, background="#d4d4d4", text="Tamanho")
        self.tamanho_label.grid(row=0, column=0, padx=5)

        self.tamanho_sudoku_var = tk.StringVar(value=str(self.tamanho_sudoku))
        self.tamanho_entrada = tk.Entry(painel_principal, textvariable=self.tamanho_sudoku_var, width=5)
        self.tamanho_entrada.grid(row=0, column=1, padx=5)

        self.botao_gerar = tk.Button(painel_principal, text="Gerar", command=lambda: self.criar_tabuleiro())
        self.botao_gerar.grid(row=0, column=2, padx=5)

        self.botao_resolver = tk.Button(painel_principal, text="Resolver", command=lambda: functions.preencher_sudoku(self, self.sudoku, 0, resolver=True))
        self.botao_resolver.grid(row=0, column=3, padx=5)

        self.criar_tabuleiro()
    
    def criar_tabuleiro(self):
        self.ja_resolvido = False
        self.entradas = []
        self.sudoku = functions.criar_sudoku(self)

        for componentes in self.painel_grade.winfo_children():
            componentes.destroy()

        if len(self.sudoku) == 0:
            return
        
        for linha in range(self.tamanho_sudoku):
            linhas_entradas = []
            for coluna in range(self.tamanho_sudoku):
                valor = self.sudoku[linha][coluna]

                entrada = tk.Entry(self.painel_grade, width=4, justify="center", font=("Arial", 12), relief="solid", bd=1, background="#f0f0f0")
                entrada.grid(row=linha, column=coluna, padx=0, pady=0, ipady=8)

                if valor != 0:
                    entrada.insert(0, str(valor))
                    entrada.config(state="disabled", disabledbackground="white", disabledforeground="black", cursor="arrow")

                linhas_entradas.append(entrada)
            
            self.entradas.append(linhas_entradas)

    def atualizar_tabuleiro(self, tabuleiro):
        tamanho = len(tabuleiro)
        for linha in range(tamanho):
            for coluna in range(tamanho):
                entrada = self.entradas[linha][coluna]
                if entrada["state"] == "normal":
                    entrada.delete(0, tk.END)
                    entrada.insert(0, str(tabuleiro[linha][coluna]))
                    entrada.config(state="readonly", readonlybackground="#9fff75")
                else:
                    entrada.config(disabledbackground="#cccccc")