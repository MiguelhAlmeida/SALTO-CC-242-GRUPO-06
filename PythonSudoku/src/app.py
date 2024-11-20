import tkinter as tk
from tkinter import messagebox
from main import validate_input, reset_matrix, populate_random_cells

root = tk.Tk()
root.title("Sudoku 3x3")

root.geometry("400x400")

completion_label = tk.Label(root, text="", font=("Arial", 14), fg="green")
completion_label.grid(row=3, column=0, columnspan=3, pady=10)

def show_concluded_message(msg):
    completion_label.config(text=msg)

def show_error(msg):
    messagebox.showerror("Erro", msg)

entries = [[None for _ in range(3)] for _ in range(3)]

for i in range(3):
    for j in range(3):
        entry = tk.Entry(root, width=5, justify='center', font=("Arial", 14))
        entry.grid(row=i, column=j, padx=15, pady=15, sticky="nsew")
        entry.insert(0, '0')

        entry.bind("<FocusOut>", lambda event, row=i, col=j: validate_input(entries, row, col, show_concluded_message, show_error))

        entries[i][j] = entry

reset_button = tk.Button(root, text="Resetar", command=lambda: reset_matrix(entries, show_concluded_message, show_error), font=("Arial", 14))
reset_button.grid(row=4, column=0, columnspan=3, pady=20)

root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)
root.grid_columnconfigure(2, weight=1)

reset_matrix(entries, show_concluded_message, show_error)

root.mainloop()
