import tkinter as tk
from tkinter import messagebox

def reset_matrix(entries):
    for i in range(2):
        for j in range(2):
            entries[i][j].delete(0, tk.END)
            entries[i][j].insert(0, '0')

def validate_input(entries, row, col):
    entry = entries[row][col]
    value = entry.get()

    try:
        value_int = int(value)

        if value_int:
            if (value_int < 1) or (value_int > 4):
                entry.delete(0, tk.END)
                entry.insert(0, '0')
                show_error("O número não pode ser inferior a 1 ou superior a 4")
        else:
            entry.delete(0, tk.END)
            entry.insert(0, '0')
            show_error("O campo foi preenchido com um valor incorreto")
    except ValueError:
        show_error("Erro ao validar número")

def show_error(msg):
    messagebox.showerror("Erro", msg)

if __name__ == "__main__":

    root = tk.Tk()
    root.title("Teste de Funções")

    entries = [[tk.Entry(root, width=5, justify='center') for _ in range(2)] for _ in range(2)]
    
    for i in range(2):
        for j in range(2):
            entries[i][j].grid(row=i, column=j, padx=10, pady=10)
            entries[i][j].insert(0, '0')

    reset_matrix(entries)

    entries[0][0].insert(0, '5')
    validate_input(entries, 0, 0)

    root.mainloop()
