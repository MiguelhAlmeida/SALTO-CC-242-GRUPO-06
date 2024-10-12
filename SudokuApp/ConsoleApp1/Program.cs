using System;

namespace SudokuApp
{
    public class Program
    {
        public static void Main()
        {
            while (true)
            {
                int tamanho = ObterTamanhoMatriz();

                Sudoku sudoku = new(tamanho);
                sudoku.GeraGrade();
                sudoku.Exibir();

                if (!DesejaContinuar())
                {
                    break;
                }
            }

            Console.WriteLine("Finalizado! Pressione qualquer tecla para sair.");
            Console.ReadKey();
        }

        private static int ObterTamanhoMatriz()
        {
            int tamanho;
            while (true)
            {
                Console.WriteLine();
                Console.Write("Digite o tamanho da matriz de Sudoku (3 a 32): ");
                string? numero = Console.ReadLine();

                if (int.TryParse(numero, out tamanho) && tamanho >= 3 && tamanho <= 32)
                {
                    return tamanho;
                }
                else
                {
                    Console.WriteLine("Por favor, digite um valor válido entre 3 e 32.");
                }
            }
        }

        private static bool DesejaContinuar()
        {
            int opcao;
            while (true)
            {
                Console.WriteLine();
                Console.WriteLine("Deseja montar outra grade? ");
                Console.WriteLine("1. Sim.");
                Console.WriteLine("2. Não.");
                string? resposta = Console.ReadLine();

                if (int.TryParse(resposta, out opcao) && (opcao == 1 || opcao == 2))
                {
                    return opcao == 1;
                }
                else
                {
                    Console.WriteLine("Por favor, insira 1 para fazer outra grade ou 2 para fechar.");
                }
            }
        }
    }

    public class Sudoku
    {
        public int[,] Matriz { get; private set; }
        public int Tamanho { get; private set; }

        public Sudoku(int tamanho)
        {
            Tamanho = tamanho;
            Matriz = new int[tamanho, tamanho];
        }

        public void GeraGrade()
        {
            PreencherMatriz(0, 0);
        }

        private bool PreencherMatriz(int linha, int coluna)
        {

            if (coluna == Tamanho)
            {
                coluna = 0;
                linha++;
            }


            if (linha == Tamanho)
            {
                return true;
            }


            for (int num = 1; num <= Tamanho; num++)
            {
                if (Valido(num, linha, coluna))
                {
                    Matriz[linha, coluna] = num;


                    if (PreencherMatriz(linha, coluna + 1))
                    {
                        return true;
                    }

                    Matriz[linha, coluna] = 0;
                }
            }

            return false;
        }

        private bool Valido(int num, int linha, int coluna)
        {

            for (int i = 0; i < Tamanho; i++)
            {
                if (Matriz[linha, i] == num || Matriz[i, coluna] == num)
                {
                    return false;
                }
            }

            int blocoSize = (int)Math.Sqrt(Tamanho);
            int inicioLinha = (linha / blocoSize) * blocoSize;
            int inicioColuna = (coluna / blocoSize) * blocoSize;

            for (int i = 0; i < blocoSize; i++)
            {
                for (int j = 0; j < blocoSize; j++)
                {
                    if (Matriz[inicioLinha + i, inicioColuna + j] == num)
                    {
                        return false;
                    }
                }
            }

            return true; // O número é válido
        }

        public void Exibir()
        {
            for (int i = 0; i < Tamanho; i++)
            {
                for (int j = 0; j < Tamanho; j++)
                {
                    Console.Write(Matriz[i, j] + " ");
                }
                Console.WriteLine();
            }
        }
    }
}
