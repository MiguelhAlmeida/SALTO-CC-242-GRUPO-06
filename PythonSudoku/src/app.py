import tkinter as tk
from main import validate_input, reset_matrix

root = tk.Tk()
root.title("Matriz 2x2")

entries = [[None for _ in range(2)] for _ in range(2)]

for i in range(2):
    for j in range(2):
        entry = tk.Entry(root, width=5, justify='center')
        entry.grid(row=i, column=j, padx=10, pady=10)
        entry.insert(0, '0')
        entry.bind("<FocusOut>", lambda event, row=i, col=j: validate_input(entries, row, col))
        entries[i][j] = entry

reset_button = tk.Button(root, text="Resetar", command=lambda: reset_matrix(entries))
reset_button.grid(row=2, column=0, columnspan=2, pady=10)

reset_matrix(entries)

root.mainloop()
