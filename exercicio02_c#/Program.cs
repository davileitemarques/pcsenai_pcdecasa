using System;

class Program
{
    static void Main ()
    {
        
        int coletas = 10;
        int totalMoedas = 0;

        while (coletas > 0)
        {   

            coletas = coletas - 1;
            Console.Write("Quantidade de moedas coletadas: ");
            int moedasFinais = int.Parse(Console.ReadLine() ?? "0");
            totalMoedas += moedasFinais;

            Console.WriteLine("Total de moedas adquiridas : " + totalMoedas);

            if (totalMoedas >= 100)
            {
                Console.WriteLine("Parabens!, voce ganhou uma vida extra");
            }   
        }       
    }
}
