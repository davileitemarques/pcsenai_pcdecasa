
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
media_exercicios = float(input("Digite a media dos exercicios no teste: "))

media_aproveitamento = (nota1 + nota2 * 2 + nota3 * 3 + media_exercicios) / 7

if media_aproveitamento >= 9:
   print("Voce tirou nota A!!")
elif media_aproveitamento < 9 and media_aproveitamento >= 7.5:
   print("Voce tirou nota B!!")
elif media_aproveitamento < 7.5 and media_aproveitamento >= 6:
   print("Voce tirou nota C!!")
else:
   print("Voce tirou nota D!!")