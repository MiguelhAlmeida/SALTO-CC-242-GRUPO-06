using System;

  namespace Advinhenumero
  {
    class Program
    {
      static void Main(string [] args)
      {
        int numbermin = 1;
        int numbermax = 10;

        Random random = new Random();
        int secretnumber = random.Next(numbermin, numbermax + 1);

        int chute = 0;
        int tentativas = 0;

        Console.WriteLine("Advinhe o número");
        Console.WriteLine($"Tente advinhar um número que eu estou pensando entre {numbermin} e {numbermax}.");

        while (chute != secretnumber)
        {
          tentativas++;

          Console.WriteLine("Digite seu palpite: ");
          string input = Console.ReadLine();

          if(int.TryParse(input, out chute))
          {
            if (chute < numbermin || chute > numbermax)
            {
              Console.WriteLine($"Número fora da escala definida. Tente outro número entre {numbermin} e {numbermax}: ");
            }
            else if (chute < secretnumber)
            {
              Console.WriteLine("Iiiih, passou longe kkkkkkkk. Número baixo, tente outro: ");
            }
            else if (chute > secretnumber)
            {
              Console.WriteLine("Vai aonde mano? Número alto, Tente outro: ");
            }
            else
            {
              Console.WriteLine($"Aeee, acertou! Você usou {tentativas} tentativas.");
            }
          }
          else
          {
            Console.WriteLine("Não entendi, digite um número vállido.");
          }
        }
      }
    }
  }