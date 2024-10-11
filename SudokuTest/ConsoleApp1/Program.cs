namespace ConsoleApp1
{
    public class GradeSudoku
    {
        public int[,] grade { get; set; } // Grade da matriz
        public int tamanho { get; set; } // Tamanho da matriz

        public void GeraGrade()
        {
            //this.tamanho = tamanho;
            //grade = new int[tamanho * tamanho];

            //for (int i = 0; i < tamanho; i++)
                //for (int j = 0; j < tamanho; j++)
                    //Preencher(i, j);
        }

        // Grade
        public GradeSudoku(int tamanho)
        {
            this.tamanho = tamanho;
            //grade = new int[tamanho * tamanho];
            grade = new int[tamanho, tamanho];

            //GeraGrade();
            //PreenchimentoComValidacoes();
        }

        /*
        // Preenche a matriz com validações de linha, coluna e bloco
        private void PreenchimentoComValidacoes()
        {
            if (!Preencher(0, 0))
            {
                Console.WriteLine("Não foi possível preencher a matriz.");
            }
        }*/

        /*
        private bool Preencher(int linha, int coluna)
        {
            if (linha == tamanho) // Se todas as linhas foram preenchidas
                return true;

            if (coluna == tamanho) // Se a coluna ultrapassou o tamanho, irá à próxima linha
            {
                return Preencher(linha + 1, 0);
            }
            Console.WriteLine($"Tentando preencher: Linha {linha}, Coluna {coluna}");

            // Preenchendo a partir do tamanho da matriz
            for (int num = 1; num <= tamanho; num++)
            {
                if (Valido(num, linha, coluna))
                {
                    grade[linha * tamanho + coluna] = num; // Coloca o número na grade

                    // Preenchendo outra célula
                    if (Preencher(linha, coluna + 1))
                    {
                        return true; // Okay para próxima célula preenchida
                    }

                    // Se não conseguir, dá um reset tentando fazer outra ação 
                    grade[linha * tamanho + coluna] = 0;
                }
            }
            return false; // Nenhum número válido
        }

        private bool Valido(int num, int linha, int coluna)
        {
            Console.WriteLine($"Verificando se o número {num} pode ser colocado na linha {linha}, coluna {coluna}.");
            // Verifica se o número já está na linha ou coluna
            for (int i = 0; i < tamanho; i++)
            {
                if (grade[linha * tamanho + i] == num || grade[i * tamanho + coluna] == num)
                {
                    Console.WriteLine($"O número {num} já existe na linha {linha} ou na coluna {coluna}.");
                    return false; // Se já existir, retorna falso
                }
            }

            // Verifica o bloco para ver se não há repetições
            int bloco = (int)Math.Sqrt(tamanho); // Raiz quadrada para determinar o tamanho do bloco
            int inicioLinha = (linha / bloco) * bloco;
            int inicioColuna = (coluna / bloco) * bloco;

            for (int i = 0; i < bloco; i++)
            {
                for (int j = 0; j < bloco; j++)
                {
                    if (grade[(inicioLinha + i) * tamanho + (inicioColuna + j)] == num)
                    {
                        Console.WriteLine($"O número {num} já existe no bloco que começa em ({inicioLinha}, {inicioColuna}).");
                        return false;
                    }
                }
            }
            Console.WriteLine($"O número {num} pode ser colocado na linha {linha}, coluna {coluna}.");
            return true; // Se passou em todas as validações
        }

        // Exibição da Matriz
        public void Exibir()
        {
            for (int i = 0; i < tamanho; i++)
            {
                for (int j = 0; j < tamanho; j++)
                {
                    Console.Write(grade[i * tamanho + j] + " | ");
                }
                Console.WriteLine();
            }
        }*/
    }

    public class Program
    {
        

        public static void Main()
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
                //sudoku.Exibir();

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
