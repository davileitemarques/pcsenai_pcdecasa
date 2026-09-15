using System;

class Program
{
    static void Main ()
    {
        Console.Write("Digite o dano base: ");
        int danoBase = int.Parse(Console.ReadLine() ?? "0");
        Random random = new Random();
        int numAleatorio = random.Next(1, 101);
        Console.WriteLine($"Numero gerado: {numAleatorio}");
        if (numAleatorio > 80)
        {
            int danoFinal = danoBase * 2;
            Console.WriteLine("Dano base: " + danoBase);
            Console.WriteLine("Critico");
            Console.WriteLine("Dano causado: " + danoFinal);
        }
        else
        {
            int danoFinal = danoBase;
            Console.WriteLine("Dano base: " + danoBase);
            Console.WriteLine("Dano causado: " + danoFinal);
        }
    }
}
