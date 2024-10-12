def criar_tabuleiro_vazio():
    return [[0 for _ in range(9)] for _ in range(9)]

def exibir_tabuleiro(tabuleiro):
    for linha in tabuleiro:
        print(linha)

tabuleiro = criar_tabuleiro_vazio()
exibir_tabuleiro(tabuleiro)