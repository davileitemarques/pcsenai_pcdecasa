
dias = int(input("Digite a quantidade de dias que voce usou o carro: "))
km = int(input("Digite a quantidade de quilometros rodados com o carro: "))

preco_dias = dias * 120
preco_km = km * 0.15
precofinal = preco_dias + preco_km

print(f"O preco a pagar pelo aluguel do carro é: R${precofinal}")