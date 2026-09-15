using System;
using System.Data;

class Program
{
    static void Main()
    {
        int vida = 100;

        while (vida > 0)
        {
                Console.Write("Digite o valor do dano: ");
                int dano = int.Parse(Console.ReadLine() ?? "0");

                vida = vida - dano;

                Console.WriteLine("Vida restante : " + vida);

            if (vida <= 0)
            {
                Console.WriteLine("Game over");
            }    
    
        }
    }
}
