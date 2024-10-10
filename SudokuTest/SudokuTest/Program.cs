using sudokuClass01;
using System.Globalization;

namespace sudokuPrincipal
{

    public class Program
    {
        static void Main()
        {
            while (true)
            {
                int tamanho;

                while (true)
                {
                    Console.WriteLine();
                    Console.Write("Digite o tamanho da matriz de Sudoku: ");
                    string numero = Console.ReadLine();

                    // Convertendo a string em inteiro e atribuindo o valor ao int tamanho usando o out; também verificando se é maior que zero.
                    if (int.TryParse(numero, out tamanho) && tamanho > 0)
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Por favor, digite um valor válido.");
                    }
                }

                // Cria a grade.
                GradeSudoku sudoku = new(tamanho);

                Console.WriteLine();
                Console.WriteLine("Matriz preenchida: ");
                // Exibição da matriz.
                sudoku.Exibir();

                // Caso o usuário deseje montar mais uma grade e validação de opções
                int opcao;
                while (true)
                {
                    Console.WriteLine();
                    Console.WriteLine("Deseja montar outra grade? ");
                    Console.WriteLine("1. Sim.");
                    Console.WriteLine("2. Não.");
                    Console.WriteLine();
                    string resposta = Console.ReadLine();

                    // Convertendo em inteiro e validando somente duas opções (1 ou 2)
                    if (int.TryParse(resposta, out opcao) && (opcao == 1 || opcao == 2))
                    {
                        break;
                    }
                    else
                    {
                        Console.WriteLine("Por favor, insira 1 para fazer outra grade ou 2 para fechar.");
                    }
                }

                // Se a opção for 2, o programa encerra.
                if (opcao == 2)
                {
                    break;
                }
                Console.WriteLine();
            }
            Console.WriteLine("Finalizado! Pressione qualquer tecla para sair.");
            Console.ReadKey(); 
        }
    }
}
