import unittest
from unittest.mock import MagicMock
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from main import validate_input, reset_matrix, populate_random_cells, is_valid_sudoku, check_if_all_filled


class TestSudokuFunctions(unittest.TestCase):
    def setUp(self):
        self.entries = [[MagicMock() for _ in range(3)] for _ in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.entries[i][j].get.return_value = '0'
                self.entries[i][j].delete.return_value = None
                self.entries[i][j].insert.return_value = None

    def test_validate_input_invalid_value(self):
        row, col = 1, 1
        self.entries[row][col].get.return_value = '4' 
        validate_input(self.entries, row, col, MagicMock(), MagicMock())
        
        self.entries[row][col].insert.assert_called_with(0, '0')

    def test_check_if_all_filled(self):
        for i in range(3):
            for j in range(3):
                self.entries[i][j].get.return_value = '1'
        filled = check_if_all_filled(self.entries)
        self.assertTrue(filled)

    def test_populate_random_cells(self):
        for row in self.entries:
            for entry in row:
                entry.insert = MagicMock()

        populate_random_cells(self.entries, num_cells=2)
        
        filled_values = [entry.insert.call_args[0][1] for row in self.entries for entry in row if entry.insert.called]
        
        self.assertEqual(len(filled_values), 2)
        self.assertTrue(all(value in ['1', '2', '3'] for value in filled_values))


    def test_reset_matrix(self):
        show_message = MagicMock()
        show_error = MagicMock()

        reset_matrix(self.entries, show_message, show_error)

        for i in range(3):
            for j in range(3):
                self.entries[i][j].insert.assert_any_call(0, '0')

    def test_is_valid_sudoku_valid(self):
        row, col = 0, 0
        self.entries[row][col].get.return_value = '1'

        valid = is_valid_sudoku(self.entries, row, col, 1)
        self.assertTrue(valid)

    def test_is_valid_sudoku_invalid(self):
        self.entries[0][0].get.return_value = '1'
        self.entries[0][1].get.return_value = '1'  

        valid = is_valid_sudoku(self.entries, 0, 2, 1)
        self.assertFalse(valid)

if __name__ == '__main__':
    unittest.main()
