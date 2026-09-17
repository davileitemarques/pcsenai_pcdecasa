using System;

class Program
{
    static void Main()
    {
        // 1. Criar um vetor (array) de strings com 5 posições
        string[] inventario = new string[5];

        Console.WriteLine("CADASTRO DE ITENS NO INVENTÁRIO");

        // 2. Permitir armazenar nomes de itens (lendo do usuário)
        for (int i = 0; i < inventario.Length; i++)
        {
            Console.Write($"Digite o nome do item {i + 1}: ");
            inventario[i] = Console.ReadLine();
        }

        Console.WriteLine("INVENTÁRIO DE ITENS");

        // 3. Exibir todos os itens cadastrados
        for (int i = 0; i < inventario.Length; i++)
        {
            // (i + 1) serve para a contagem começar em 1 na tela em vez de 0
            Console.WriteLine($"{i + 1}\t{inventario[i]}");
        }
    }
}