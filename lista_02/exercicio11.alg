algoritmo "exercicio11"

var
preco, desconto, precofinal: real
inicio
escreva("Preço do seu produto: ")
leia(preco)
escreva("Desconto aplicado ao produto: ")
leia(desconto)

precofinal <- preco * (1 - desconto / 100)

escreva("Seu preço final é: ", precofinal:2:2)
fimalgoritmo
