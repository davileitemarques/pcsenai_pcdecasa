print ("Hello, World")

#Entrada de dados
carros_vendidos = int(input("Digite o numero de carros vendidos: "))
salario_fixo = float(input("Digite seu salario fixo: "))
valor_total = float(input("Digite o valor total de vendas: "))
valor_carro = float(input("Digite sua comissao que voce recebe a cada carro vendido: "))

#Calculo da comissao de vendas e de carros
comissao = valor_total * 0.05
comissao_carros = carros_vendidos * valor_carro

#Calculo do salario final
salario_final = salario_fixo + comissao
total_final = salario_final + comissao_carros

#Saida de dados
print(f"O salario final é: {total_final:.2f}")

