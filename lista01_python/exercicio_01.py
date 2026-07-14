#Solicita o valor da base e da altura do triangulo para o usario
base = float(input("Digite a base do triangulo: "))
altura = float(input("Digite a altura do triangulo: "))
#Calcula a area do triangulo
area = (base * altura) / 2
#Imprime o resultado
print(f"A área de triangulo é de {area:.2f} metros quadrados")