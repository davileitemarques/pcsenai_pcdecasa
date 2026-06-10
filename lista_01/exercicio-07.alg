algoritmo "exercicio07"

var
n1, n2, n3: inteiro
inicio
escreva("Seu primeiro numero: ")
leia(n1)
escreva("Seu segundo numero: ")
leia(n2)
escreva("Seu terceiro numero: ")
leia(n3)

se (n1 > n2) e (n2 > n3) entao
escreval("n1'''n2'''n3")
senao
se (n2 > n1) e (n1 > n3) entao
escreval("n2'''n1'''n3")
senao
se (n3 > n1) e (n1 > n2) entao
escreval("n3'''n1'''n2")
senao
se (n1 > n3) e (n3 > n2) entao
escreval("n1'''n3'''n2")
senao
se (n2 > n3) e (n3 > n1) entao
escreval("n2'''n3'''n1")
senao
se (n3 > n2) e (n2 > n1) entao
escreval("n3'''n2'''n1")
fimse
fimse
fimse
fimse
fimse
fimse
fimalgoritmo
