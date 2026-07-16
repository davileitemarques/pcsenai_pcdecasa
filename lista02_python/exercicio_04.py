#Pedindo a distancia que o usuario deseja percorrer
distancia = int(input("Digite a distancia desejada a percorrer (em km): "))
#Adicionando os valores as variaveis por meio de condicionais
if distancia <= 200:
    preco = distancia * 0.50
#Imprimindo o preço da viagem caso for menor ou igual a 200km
    print(f"O preço a pagar pela viagem é de R${preco}")
else:
#Se nao for menor, imprimindo um resultado diferente
    preco = distancia * 0.45
    print(f"O preço a pagar pela viagem é de R${preco}")