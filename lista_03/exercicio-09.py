
inicio_xadrez = int(input("Digite o horario em que a partida começou (em horas): "))
fim_xadrez = int(input("Digite o horario em que a partida terminou (em horas): "))

if inicio_xadrez < fim_xadrez:
    duracao = fim_xadrez - inicio_xadrez
    print(f"A duracao da partida foi de {duracao} horas")
else:
    duracao = (24 - inicio_xadrez) + fim_xadrez
    print(f"A duracao da partida foi de {duracao} horas") 

  