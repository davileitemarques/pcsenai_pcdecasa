using System;

class Program
{
    static void Main ()
    {
// 1. Criar variáveis de controle
        int experiencia = 0;
        int nivel = 1;
        int xpPorInimigo = 25; // Exemplo de XP ganha por inimigo derrotado

        Console.WriteLine($"[Início] Nível: {nivel} | Experiência: {experiencia}");

        // Simulação de derrotar 6 inimigos
        for (int i = 1; i <= 6; i++)
        {
            // 2. A cada inimigo derrotado, adicionar experiência
            experiencia += xpPorInimigo;
            Console.WriteLine($"Inimigo {i} derrotado! +{xpPorInimigo} XP ganha. (XP atual: {experiencia})");

            // 3. Quando atingir 100 pontos (ou mais)
            if (experiencia >= 100)
            {
                // Subir de nível
                nivel++;
                
                // Reiniciar a experiência (se sobrou XP extra, subtrai 100; senão zera com = 0)
                experiencia -= 100; 

                Console.WriteLine($"Você subiu para o Nível {nivel}! ***");
                Console.WriteLine($"*** XP atualizada: {experiencia} ***");
            }
        }
    }
}