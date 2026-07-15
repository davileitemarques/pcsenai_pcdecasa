from math import sqrt

n1 = int(input("Digite um numero inteiro positivo: "))
n2 = int(input("Digite outro numero inteiro positivo: "))

media_geo = sqrt(n1 * n2)
if n2 != 0:
   cubo = n2 ** 3
   print(f"O cubo do segundo numero é {cubo}")
   print(f"A media geografica é {media_geo:.2f}")
else:
   print("Não foi possivel fazer as operações")