algoritmo "exercicio_08"

var
numeroum, numerodois: real
adicao, subtracao, divisao, multiplicacao: real
inicio
escreva("Digite o primeiro numero: ")
leia(numeroum)
escreva("Digite o segundo numero: ")
leia(numerodois)

adicao <- numeroum + numerodois
subtracao <- numeroum - numerodois

se numerodois <> 0 entao
divisao <- numeroum / numerodois
multiplicacao <- numeroum * numerodois

escreval("Soma: ", adicao:0:2)
escreval("Subtra��o: ", subtracao:0:2)
escreval("Divis�o: ", divisao:0:2)
escreval("Multiplica��o: ", multiplicacao:0:2)
senao
escreva("Nao foi possivel efetuar a opera��o")
fimse
fimalgoritmo
