import unittest
import sys
import os
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
sys.path.append(SRC_DIR)
from main import SudokuApp
import tkinter as tk

class TestSudoku(unittest.TestCase):

    def setUp(self):
        """Configura uma instância básica da aplicação para testes."""
        self.root = tk.Tk()
        self.app = SudokuApp(self.root)
    
    def tearDown(self):
        """Fecha a instância do tkinter após o teste."""
        self.root.destroy()

    def test_is_valid_row(self):
        """Teste para validar números duplicados na mesma linha."""
        self.app.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        # Adicionar 3 na posição (0, 2) (duplicado na linha)
        self.assertFalse(self.app.is_valid(3, 0, 2))

    def test_is_valid_column(self):
        """Teste para validar números duplicados na mesma coluna."""
        self.app.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        # Adicionar 9 na posição (2, 0) (duplicado na coluna)
        self.assertFalse(self.app.is_valid(9, 2, 0))

    def test_is_valid_subgrid(self):
        """Teste para validar números duplicados no mesmo subgrid."""
        self.app.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        # Adicionar 9 na posição (1, 1) (duplicado no subgrid 3x3 superior esquerdo)
        self.assertFalse(self.app.is_valid(9, 1, 1))

    def test_is_valid_true(self):
        """Teste para verificar se um número válido passa."""
        self.app.grid = [
            [5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 7, 9]
        ]
        # Adicionar 2 na posição (0, 2) (válido)
        self.assertTrue(self.app.is_valid(2, 0, 2))

if __name__ == "__main__":
    unittest.main()
