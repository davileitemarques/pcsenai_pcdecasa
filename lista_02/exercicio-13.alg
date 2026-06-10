algoritmo "exercicio13"

var
compra, pago, troco: real
inicio
escreva("Valor da compra: ")
leia(compra)
escreva("Valor pago: ")
leia(pago)

se compra <> pago entao
troco <- compra - pago
escreval("O valor do troco é: ", troco)
senao
escreval("Sem troco")

fimse
fimalgoritmo
