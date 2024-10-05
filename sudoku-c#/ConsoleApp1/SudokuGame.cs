using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class SudokuGame
    {
        private SudokuMatriz grid;

        public SudokuGame()
        {
            grid = new SudokuMatriz();
        }

        public void Start()
        {
            grid.GeracaoSudoku();
            grid.DisplayGrade();

            Console.WriteLine("Bem vindo ao Sudoku 9x9! Preencha a grade com números de 1 a 9");
            Play();

            if (grid.resolvido())
                Console.WriteLine("Parabéns! Você conseguiu resolver o Sudoku");
            else
                Console.WriteLine("Sudoku não foi resolvido corretamente");
        }

        private void Play()
        {
            int linha, coluna, num;

            while (!grid.resolvido())
            {
                Console.WriteLine("Escolha entre as linha (1 e 9): ");
                linha = Convert.ToInt32(Console.ReadLine() ) - 1;

                Console.WriteLine("Escolha entre as colunas (1 e 9): ");
                coluna = Convert.ToInt32(Console.ReadLine() ) - 1;

                if (grid.preenchida(linha, coluna) > 0) 
                {
                    Console.WriteLine("Essa célula já foi preenchida, tente novamente.");
                    continue;
                }
                else if (grid.preenchida(linha, coluna) == -1)
                {
                    Console.WriteLine("Posição invalida");
                    continue;
                }

                Console.WriteLine("Insira um número de (1 a 9): ");
                num = Convert.ToInt32(Console.ReadLine());

                if (grid.validacao(num, linha, coluna)) 
                { 
                    grid.InserirCelula(linha, coluna, num);
                    grid.DisplayGrade();
                }
                else
                {
                    Console.WriteLine("Entrada invalida, tente novamente");
                }
            }
        }

    }
}
