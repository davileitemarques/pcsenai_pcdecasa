algoritmo "exercicio_02"

var
base, altura, resultado: real

inicio
escreva("Base do seu retangulo: ")
leia(base)
escreva("Altura do seu retangulo: ")
leia(altura)

se (base <> 0) e (altura <> 0) entao
resultado <- base * altura
escreval("A area do seu retangulo é: ", resultado:2:2)
senao
escreva("Nao foi possivel efetuar a operação")
fimse
fimalgoritmo
