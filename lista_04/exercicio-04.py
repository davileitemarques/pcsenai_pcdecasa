
time1 = str(input("Escreva o nome do primeiro time: "))
gols1 = int(input("Coloque quantos gols fez o primeiro time: "))
time2 = str(input("Escreva o nome do segundo time: "))
gols2 = int(input("Coloque quantos gols fez o segundo time: "))

if gols1 > gols2:
    print(f"{time1} foi o vencedor!!")
#Os dois simbolos de igual sao usados para uma comparação, um único simbolo de igual significa atribuição
elif gols1 == gols2:
    print(f"Não houve vencedor, Empate")
else:
    print(f"{time2} foi o vencedor!!")