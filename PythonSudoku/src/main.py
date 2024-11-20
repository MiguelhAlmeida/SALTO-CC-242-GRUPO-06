import random

def reset_matrix(entries, show_message, show_error):
    for i in range(3):
        for j in range(3):
            entries[i][j].delete(0, 'end')
            entries[i][j].insert(0, '0')
    
    populate_random_cells(entries, num_cells=2, show_message=show_message, show_error=show_error)

def validate_input(entries, row, col, show_message, show_error):
    entry = entries[row][col]
    value = entry.get()

    if value == '0' or value == '':
        return
    
    if not value.isdigit():
        entry.delete(0, 'end')
        entry.insert(0, '0')
        show_error("Por favor, insira um número válido.")
        return
    
    try:
        value_int = int(value)

        if value_int < 1 or value_int > 3:
            entry.delete(0, 'end')
            entry.insert(0, '0')
            show_error("O número deve ser entre 1 e 3.")
            return
        
        if not is_valid_sudoku(entries, row, col, value_int):
            entry.delete(0, 'end')
            entry.insert(0, '0')
            show_error("Número repetido na linha ou coluna.")
            return
        
        if check_if_all_filled(entries):
            show_message("Concluído")
        
    except ValueError:
        entry.delete(0, 'end')
        entry.insert(0, '0')
        show_error("Erro ao validar número.")

def is_valid_sudoku(entries, row, col, value):
    for i in range(3):
        if i != col and entries[row][i].get() != '0' and int(entries[row][i].get()) == value:
            return False
    
    for i in range(3):
        if i != row and entries[i][col].get() != '0' and int(entries[i][col].get()) == value:
            return False
    
    return True

def check_if_all_filled(entries):
    for i in range(3):
        for j in range(3):
            value = entries[i][j].get()
            if not value.isdigit() or int(value) < 1 or int(value) > 3:
                return False
    return True

def populate_random_cells(entries, num_cells=2, show_message=None, show_error=None):
    values = [1, 2, 3]
    random.shuffle(values)

    filled = 0
    while filled < num_cells:
        row = random.randint(0, 2)
        col = random.randint(0, 2)

        if entries[row][col].get() == '0':
            value = values[filled]
            if is_valid_sudoku(entries, row, col, value): 
                entries[row][col].delete(0, 'end')
                entries[row][col].insert(0, str(value))
                filled += 1

    if check_if_all_filled(entries) and show_message:
        show_message("Concluído")
