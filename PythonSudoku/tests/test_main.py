import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))
from src.main import validate_input, reset_matrix
import pytest
from unittest.mock import MagicMock


def test_validate_input_valid_value():
    entry = MagicMock()
    entry.get.return_value = '3'

    entries = [[entry, entry], [entry, entry]]
    validate_input(entries, 0, 0)

    entry.delete.assert_not_called()
    entry.insert.assert_not_called()

def test_validate_input_invalid_value_low():
    entry = MagicMock()
    entry.get.return_value = '0'

    entries = [[entry, entry], [entry, entry]]
    validate_input(entries, 0, 0)

    entry.delete.assert_called_once()
    entry.insert.assert_called_once_with(0, '0')
def test_validate_input_invalid_value_high():
    entry = MagicMock()
    entry.get.return_value = '5'

    entries = [[entry, entry], [entry, entry]]
    validate_input(entries, 0, 0)

    entry.delete.assert_called_once()
    entry.insert.assert_called_once_with(0, '0')

if __name__ == "__main__":
    pytest.main()