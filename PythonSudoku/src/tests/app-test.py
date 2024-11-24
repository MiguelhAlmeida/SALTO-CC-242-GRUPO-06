import sys
import os
import tkinter as tk
from tkinter import messagebox

# Adiciona o diretório 'src' ao caminho do Python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
sys.path.append(SRC_DIR)

# Importa a função do aplicativo
from app import abrir_aplicativo

def testar_abrir_aplicativo():
    """
    Testa se o aplicativo Sudoku abre e fecha corretamente.
    """
    try:
        # Inicia o aplicativo
        abrir_aplicativo(tests=False)  # Executa normalmente o Sudoku
        
        # Mostra mensagem de sucesso após o encerramento
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal
        messagebox.showinfo("Teste de Aplicativo", "O aplicativo foi executado e encerrado com sucesso.")
        root.destroy()

        print("Teste de execução do aplicativo: SUCESSO")
    except Exception as e:
        # Mostra mensagem de erro em caso de falha
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal
        messagebox.showerror("Teste de Aplicativo", f"Erro durante a execução do aplicativo: {str(e)}")
        root.destroy()

        print("Teste de execução do aplicativo: ERRO")
        raise

if __name__ == "__main__":
    testar_abrir_aplicativo()
