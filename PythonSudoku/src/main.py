import tkinter as tk
from tkinter import messagebox
import random

class SudokuApp:
    def __init__(self, root):
        print('Codigo na branch do Miguel')
        self.root = root
        self.root.title("Sudoku")
        self.grid = [[0 for _ in range(9)] for _ in range(9)]
        self.entries = [[None for _ in range(9)] for _ in range(9)]
        
        self.create_grid()
        self.generate_sudoku()
        self.fill_grid()
        
        btn_solve = tk.Button(root, text="Solve", command=self.solve_sudoku)
        btn_solve.grid(row=10, column=0, columnspan=9)
        
    def create_grid(self):
        for i in range(9):
            for j in range(9):
                entry = tk.Entry(self.root, width=5, font=('Arial', 18), justify='center')
                entry.grid(row=i, column=j)
                self.entries[i][j] = entry

    def generate_sudoku(self):
        self.fill_grid()

    def fill_grid(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    num_list = random.sample(range(1, 10), 9)  # Números de 1 a 9
                    for num in num_list:
                        if self.is_valid(num, row, col):
                            self.grid[row][col] = num
                            if self.fill_grid():  # Chamada recursiva
                                return True
                            self.grid[row][col] = 0  # Backtrack
                    return False  # Se nenhum número é válido
        return True  # Preenchimento completo

    def remove_numbers(self):
        count = 40  # Numbers to remove
        while count > 0:
            i = random.randint(0, 8)
            j = random.randint(0, 8)
            if self.grid[i][j] != 0:
                self.grid[i][j] = 0
                count -= 1

    def fill_grid(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] != 0:
                    self.entries[i][j].delete(0, tk.END)
                    self.entries[i][j].insert(0, str(self.grid[i][j]))
                    self.entries[i][j].config(state='readonly')

    def is_valid(self, num, row, col):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        
        start_row, start_col = 3 * (row // 3), 3 * (col // 3)
        for i in range(3):
            for j in range(3):
                if self.grid[start_row + i][start_col + j] == num:
                    return False
        return True

    def solve_sudoku(self):
        if self.solve():
            self.fill_grid()
        else:
            messagebox.showinfo("Info", "No solution exists!")

    def solve(self):
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    for num in range(1, 10):
                        if self.is_valid(num, row, col):
                            self.grid[row][col] = num
                            if self.solve():
                                return True
                            self.grid[row][col] = 0
                    return False
        return True

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuApp(root)
    root.mainloop()
