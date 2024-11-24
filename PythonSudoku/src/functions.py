import random
from tkinter import messagebox

def criar_sudoku(self):
    raiz = 0
    try:
        self.tamanho_sudoku = int(self.tamanho_sudoku_var.get())

        raiz = int(self.tamanho_sudoku ** 0.5)
        if raiz ** 2 != self.tamanho_sudoku:
            raise SystemError("O tamanho do sudoku deve ser um quadrado perfeito.")
    except ValueError:
        messagebox.showerror("Error!", "O tamanho do sudoku deve ser um número inteiro.")
        return []
    except SystemError as e:
        messagebox.showerror("Error!", e)
        return []

    sudoku = [
        [0 for _ in range(self.tamanho_sudoku)]
        for _ in range(self.tamanho_sudoku)
    ]

    preencher_sudoku(self, sudoku, raiz)
    remover_numeros(self, sudoku)

    return sudoku

def preencher_sudoku(self, sudoku, raiz, resolver=False):
    if self.ja_resolvido:
        messagebox.showwarning("Aviso!", "O sudoku já foi resolvido!")
        return True
    
    if raiz == 0:
        raiz = int(self.tamanho_sudoku ** 0.5)

    # o Alyfer passou por aqui :D
    for linha in range(self.tamanho_sudoku):
        for coluna in range(self.tamanho_sudoku):
            if sudoku[linha][coluna] == 0:
                for num in random.sample(range(1, self.tamanho_sudoku + 1), self.tamanho_sudoku):
                    if pode_colocar(self, sudoku, linha, coluna, num, raiz):
                        sudoku[linha][coluna] = num
                        if preencher_sudoku(self, sudoku, raiz, resolver):
                            return True
                        sudoku[linha][coluna] = 0
                return False
            
    if resolver:
        self.atualizar_tabuleiro(sudoku)
        self.ja_resolvido = True

    return True
# o Alyfer passou por aqui :D
def pode_colocar(self, sudoku, linha, coluna, valor, raiz):
    if valor in sudoku[linha]:
        return False
    
    for _linha in range(self.tamanho_sudoku):
        if sudoku[_linha][coluna] == valor:
            return False

    inicio_linha = (linha // raiz) * raiz
    inicio_coluna = (coluna // raiz) * raiz

    for _linha in range(inicio_linha, inicio_linha + raiz):
        for _coluna in range(inicio_coluna, inicio_coluna + raiz):
            if sudoku[_linha][_coluna] == valor:
                return False
        
    return True

def remover_numeros(self, sudoku):
    total_celulas = self.tamanho_sudoku * self.tamanho_sudoku
    valor_remover = total_celulas // 2
    celulas = [
        (linha, coluna) for linha in range(self.tamanho_sudoku)
        for coluna in range(self.tamanho_sudoku)
    ]
    random.shuffle(celulas)

    for indice in range(valor_remover):
        linha, coluna = celulas[indice]
        sudoku[linha][coluna] = 0