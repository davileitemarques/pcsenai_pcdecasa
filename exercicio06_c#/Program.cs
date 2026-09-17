using System;

class Program
{
    static void Main()
    {

        int heroiHp = 100;
        int monstroHp = 80;

      
        int danoHeroi = 30; 
        int danoMonstro = 15; 

        while (heroiHp > 0 && monstroHp > 0)
        {

            monstroHp -= danoHeroi;
            Console.WriteLine("Herói atacou.");
            Console.WriteLine($"Monstro HP: {monstroHp}\n");

  
            if (monstroHp <= 0)
            {
                break;
            }

            heroiHp -= danoMonstro;
            Console.WriteLine("Monstro atacou.");
            Console.WriteLine($"Herói HP: {heroiHp}\n");
        }

        if (monstroHp <= 0)
        {
            Console.WriteLine("Vitória do Herói!");
        }
        else
        {
            Console.WriteLine("O Monstro venceu!");
        }
    }
}
