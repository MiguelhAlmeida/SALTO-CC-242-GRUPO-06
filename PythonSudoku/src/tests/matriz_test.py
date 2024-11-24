import sys
import os
import tkinter as tk
from tkinter import messagebox

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SRC_DIR = os.path.abspath(os.path.join(BASE_DIR, '..'))
sys.path.append(SRC_DIR)

from app import abrir_aplicativo
from hud import Interface

def testar_tamanho_matriz():
    """
    Teste automatizado que verifica se a matriz gerada possui o tamanho informado pelo usuário.
    """
    try:
        # Variáveis de teste
        tamanho_desejado = 9 # Pode ser modificado para testar outros tamanhos
        matriz_gerada = []

        # Função de callback para capturar a matriz gerada
        def capturar_matriz(app_instance):
            nonlocal matriz_gerada
            print("Capturando a matriz gerada...")  # Debug
            matriz_gerada = app_instance.sudoku
            print(f"Matriz capturada: {matriz_gerada}")  # Debug

        # Classe de interface personalizada para teste
        class InterfaceTeste(Interface):
            def criar_tabuleiro(self):
                super().criar_tabuleiro()
                capturar_matriz(self)  # Captura a matriz ao criar o tabuleiro

        # Inicializa a interface de teste
        raiz = tk.Tk()
        app = InterfaceTeste(raiz)
        app.tamanho_sudoku_var.set(str(tamanho_desejado))  # Define o tamanho desejado
        app.criar_tabuleiro()

        # Mantém a interface ativa até que todos os widgets sejam criados
        raiz.update_idletasks()

        # Validação do tamanho da matriz gerada
        validar_tamanho_matriz(matriz_gerada, tamanho_desejado)

        # Se passou em todas as validações
        print(f"Teste de tamanho da matriz ({tamanho_desejado}x{tamanho_desejado}): SUCESSO")
        messagebox.showinfo("Teste de Matriz", "O teste da matriz foi concluído com sucesso!")

        # Fecha a janela após as validações
        raiz.destroy()

    except AssertionError as e:
        tratar_falha("Falha no teste de tamanho da matriz", e)
    except Exception as e:
        tratar_falha("Erro inesperado", e)

def validar_tamanho_matriz(matriz, tamanho_desejado):
    """Função para validar o tamanho da matriz gerada"""
    assert len(matriz) == tamanho_desejado, (
        f"Matriz gerada tem {len(matriz)} linhas, mas deveria ter {tamanho_desejado}."
    )
    for i, linha in enumerate(matriz):
        assert len(linha) == tamanho_desejado, (
            f"Erro na linha {i}: uma linha da matriz tem {len(linha)} colunas, mas deveria ter {tamanho_desejado}."
        )

def tratar_falha(mensagem, erro):
    """Função para tratar falhas e exibir mensagens de erro de forma organizada"""
    print(f"{mensagem}: FALHA - {erro}")
    root = tk.Tk()
    root.withdraw()  # Esconde a janela principal
    messagebox.showerror(mensagem, str(erro))
    root.destroy()

if __name__ == "__main__":
    testar_tamanho_matriz()
