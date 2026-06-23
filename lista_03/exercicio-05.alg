algoritmo "exercicio05"
// Função :
// Autor :
// Data : 23/06/2026
// Seção de Declarações 
var
valor_fabrica, valorfinal, distribuidor, impostos: real
inicio
escreva("Valor de fabrica do carro: ")
leia(valor_fabrica)

impostos <- valor_fabrica * (0.45)
distribuidor <- valor_fabrica * (0.28)

valorfinal <- valor_fabrica + distribuidor + impostos

escreva("O valor final do carro é:  R$", valorfinal:2:2)
fimalgoritmo
