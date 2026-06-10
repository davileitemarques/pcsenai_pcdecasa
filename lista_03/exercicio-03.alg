algoritmo "exercicio_03"

var
anos, meses, dias, final: inteiro
inicio
escreva("Digite quantos anos voce tem: ")
leia(anos)
escreva("Digite quantos meses voce tem (depois de anos): ")
leia(meses)
escreva("Digite quantos dias voce tem (depois de anos e meses): ")
leia(dias)

final <- (anos * 365) + (meses * 30) + dias

escreval("Sua idade em dias é exatamente: ", final)
fimalgoritmo
