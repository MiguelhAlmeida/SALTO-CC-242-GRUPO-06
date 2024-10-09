import tkinter as tk
from tkinter import messagebox, Label

# Função para definir os valores como 0 inicialmente
def reset_matrix():
    for i in range(2):
        for j in range(2):
            entries[i][j].delete(0, tk.END)  # Limpar o valor atual
            entries[i][j].insert(0, '0')  # Definir como 0

# Função que valida se o valor inserido é um número inteiro de 1 a 4
def valida_entrada(event, row, col):
    entry = entries[row][col]
    value = entry.get()

    if value == '':
        entry.insert(0, '0')
    else:
        try:
            int_value = int(value)
            if value != '0':
                if int_value < 1 or int_value > 4:
                    raise ValueError
        except ValueError:
            messagebox.showerror("Erro", "Por favor, insira um número inteiro entre 1 e 4.")
            entry.delete(0, tk.END)
            entry.insert(0, '0')
        else:
            check_repetidos()

# Função para verificar se há valores repetidos
def check_repetidos():
    values = []
    for i in range(2):
        for j in range(2):
            value = entries[i][j].get()
            if value != '0':  # Não verificar os campos com 0
                if value in values:
                    messagebox.showerror("Erro", f"O valor {value} está repetido.")
                    entries[i][j].delete(0, tk.END)
                    entries[i][j].insert(0, '0')
                else:
                    values.append(value)

# Criando a janela principal
root = tk.Tk()
root.title("Sudoku")

# Label centralizado
label = Label(root, text="Insira os valores para completar o sudoku", justify='center')
label.grid(row=0, column=0, columnspan=2, pady=10)  # Centraliza o label na janela

# Criando uma matriz 2x2 de campos de entrada
entries = [[None for _ in range(2)] for _ in range(2)]

for i in range(2):
    for j in range(2):
        entry = tk.Entry(root, width=5, justify='center') 
        entry.grid(row=i+1, column=j, padx=10, pady=10)
        entry.insert(0, '0')
        entry.bind("<FocusOut>", lambda event, row=i, col=j: valida_entrada(event, row, col))  # Validar após perder o foco
        entries[i][j] = entry

# Botão de reset
reset_button = tk.Button(root, text="Resetar", command=reset_matrix)
reset_button.grid(row=3, column=0, columnspan=2, pady=10)  #Centraliza o botão de reset

# Iniciar com os valores zerados
reset_matrix()

# Executar a interface
root.mainloop()
