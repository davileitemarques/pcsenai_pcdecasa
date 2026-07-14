import math

x1 = float(input("Digite a coordenada de X do primeiro ponto: "))
x2 = float(input("Digite a coordenada de X do segundo ponto: "))
y1 = float(input("Digite a coordenada de Y do primeiro ponto: "))
y2 = float(input("Digite a coordenada de Y do segundo ponto: "))

distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
distancia = math.sqrt (distancia)

print(f"A distancia entre esses dois pontos é de {distancia:.2f}")