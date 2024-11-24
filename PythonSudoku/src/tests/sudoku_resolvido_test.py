import sys
import os
import tkinter as tk

# Adiciona o diretório 'src' ao caminho do Python
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
sys.path.append(SRC_DIR)

from app import abrir_aplicativo
from hud import Interface
from functions import preencher_sudoku

def testar_sudoku_resolvido():
    """
    Teste automatizado para verificar se o Sudoku foi resolvido corretamente.
    """
    try:
        tamanho_sudoku = 9 # Define o tamanho do Sudoku para o teste
        sudoku_gerado = []

        # Função de callback para capturar o Sudoku gerado
        def capturar_sudoku(app_instance):
            nonlocal sudoku_gerado
            sudoku_gerado = app_instance.sudoku

        # Classe de interface personalizada para capturar a matriz resolvida
        class InterfaceTeste(Interface):
            def criar_tabuleiro(self):
                super().criar_tabuleiro()
                capturar_sudoku(self)  # Captura o Sudoku ao criar o tabuleiro

        # Inicializa a interface de teste
        raiz = tk.Tk()
        app = InterfaceTeste(raiz)
        app.tamanho_sudoku_var.set(str(tamanho_sudoku))  # Define o tamanho desejado
        app.criar_tabuleiro()

        # Resolve o Sudoku
        preencher_sudoku(app, sudoku_gerado, raiz=0, resolver=True)

        # Mantém a interface ativa até que todos os widgets sejam atualizados
        raiz.update_idletasks()

        # Validação: todas as células preenchidas
        for linha in sudoku_gerado:
            assert all(cell != 0 for cell in linha), (
                "Erro: O Sudoku contém células vazias (valor 0)."
            )

        # Validação: linhas, colunas e subgrades
        def validar_linhas(sudoku):
            for linha in sudoku:
                if sorted(linha) != list(range(1, tamanho_sudoku + 1)):
                    return False
            return True

        def validar_colunas(sudoku):
            for coluna in range(tamanho_sudoku):
                valores_coluna = [linha[coluna] for linha in sudoku]
                if sorted(valores_coluna) != list(range(1, tamanho_sudoku + 1)):
                    return False
            return True

        def validar_subgrades(sudoku, raiz):
            for bloco_linha in range(0, tamanho_sudoku, raiz):
                for bloco_coluna in range(0, tamanho_sudoku, raiz):
                    subgrade = []
                    for linha in range(bloco_linha, bloco_linha + raiz):
                        for coluna in range(bloco_coluna, bloco_coluna + raiz):
                            subgrade.append(sudoku[linha][coluna])
                    if sorted(subgrade) != list(range(1, tamanho_sudoku + 1)):
                        return False
            return True

        raiz_tamanho = int(tamanho_sudoku ** 0.5)

        assert validar_linhas(sudoku_gerado), "Erro: Uma ou mais linhas são inválidas."
        assert validar_colunas(sudoku_gerado), "Erro: Uma ou mais colunas são inválidas."
        assert validar_subgrades(sudoku_gerado, raiz_tamanho), "Erro: Uma ou mais subgrades são inválidas."

        # Se passou em todas as validações
        print("Teste de Sudoku Resolvido: SUCESSO")
        tk.messagebox.showinfo("Teste de Sudoku", "O teste foi concluído com sucesso!")

        # Fecha a janela após as validações
        raiz.destroy()

    except AssertionError as e:
        print(f"Teste de Sudoku Resolvido: FALHA - {e}")
        root = tk.Tk()
        root.withdraw()  # Esconde a janela principal
        tk.messagebox.showerror("Teste de Sudoku", f"Falha no teste: {e}")
        root.destroy()
        raise
    except Exception as e:
        print(f"Erro inesperado: {e}")
        raise

if __name__ == "__main__":
    testar_sudoku_resolvido()
