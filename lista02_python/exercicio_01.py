#Pedindo o preco e o desconto para o usuario digitar
preco = float(input("Digite o preco do produto: "))
desconto = float(input("Digite o desconto sobre o produto: "))
#Coloca o desconto aplicado em forma decimal e calcula o preco final
descontofinal = desconto / 100
precofinal = preco * (1 - descontofinal)
#Imprime o preço final ao usuario
print(f"O preço final do produto é: R${precofinal}")

