using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApp1
{
    internal class SudokuMatriz
    {
        int tamanhoMatriz = 9;    
        
        private int[,] grid = new int[9, 9];
        private Random random = new Random();

            public void GeracaoSudoku()
            {
                grid = new int[,]
                {
                    {0, 9, 2, 0, 7, 0, 0, 0, 6},
                    {3, 0, 5, 0, 2, 0, 7, 0, 9},
                    {6, 0, 8, 0, 5, 0, 0, 2, 0},
                    {0, 1, 0, 5, 4, 0, 6, 0, 8},
                    {4, 5, 6, 0, 0, 0, 0, 0, 0},
                    {0, 8, 0, 3, 0, 0, 2, 0, 0},
                    {5, 0, 7, 0, 0, 0, 9, 0, 0},
                    {0, 6, 0, 9, 0, 0, 0, 7, 0},
                    {0, 0, 4, 0, 1, 5, 0, 6, 0}
                };
            }

            public void DisplayGrade()
            {
                Console.WriteLine("\nGrade atual:");
                for (int i = 0; i < tamanhoMatriz; i++)
                {
                    for (int j = 0; j < tamanhoMatriz; j++)
                    {
                        Console.Write(grid[i, j] == 0 ? "_" : grid[i, j].ToString());
                        Console.Write(" ");
                    }
                    Console.WriteLine();
                }
                Console.WriteLine();
            }

            public int preenchida(int linha, int coluna)
            {   
                if (linha > (tamanhoMatriz - 1) || coluna > (tamanhoMatriz - 1) || linha < 0 || coluna < 0)
                {
                    return -1;
                }

                return grid[linha, coluna];
            }

            public void InserirCelula(int linha, int coluna, int num)
            {
                grid[linha, coluna] = num;
            }
            public bool validacao(int num, int linha, int coluna)
            {
                for (int i = 0; i < tamanhoMatriz; i++)
                {
                    if (grid[linha, i] == num || grid[i, coluna] == num)
                        return false;
                }
                return true;
            }
            
            public bool validacaoSubgrade(int linha, int coluna)
            {
                bool[] seen = new bool[10];
                
                int startLinha = (linha / 3) * 3;
                int startColuna = (coluna / 3) * 3;

                for (int i = startLinha; i < startLinha + 3; i++)
                {
                    for (int j = startColuna; j < startColuna + 3; j++)
                    {
                        int numero = grid[i, j];
                        if (numero != 0)
                        {
                            return false;
                        }
                        seen[numero] = true;
                    }
                }
                return true;
            }

            public bool resolvido()
            {
                for (int i = 0; i < tamanhoMatriz; i++)
                {
                    for (int j = 0; j < tamanhoMatriz; j++)
                    {
                        if (grid[i, j] == 0)
                            return false;
                    }
                }
                return true;
            }
        }
    }
