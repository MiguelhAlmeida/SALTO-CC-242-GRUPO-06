using System.Globalization;

namespace sudokuClass01
{
    public class GradeSudoku
    {
        private int[] grade; // Grade da matriz
        private int tamanho; // Tamanho da matriz

        // Grade
        public GradeSudoku(int tamanho)
        {
            this.tamanho = tamanho;
            grade = new int[tamanho * tamanho];
            PreenchimentoComValidacoes();
        }

        // Preenche a matriz com validações de linha, coluna e bloco
        private void PreenchimentoComValidacoes()
        {
            if (!Preencher(0, 0))
            {
                Console.WriteLine("Não foi possível preencher a matriz.");
            }
        }

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
        }
    }
}
