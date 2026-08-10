#Importei a biblioteca math
import math
#Pedi a coordenada de X e Y dos dois pontos
x1 = float(input("Digite a coordenada de X do primeiro ponto: "))
x2 = float(input("Digite a coordenada de X do segundo ponto: "))
y1 = float(input("Digite a coordenada de Y do primeiro ponto: "))
y2 = float(input("Digite a coordenada de Y do segundo ponto: "))
#Calculei a distancia
distancia = ((x2 - x1) ** 2 + (y2 - y1) ** 2)
distancia = math.sqrt (distancia)
#Imprime o resultado
print(f"A distancia entre esses dois pontos é de {distancia:.2f}")