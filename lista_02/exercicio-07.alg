algoritmo "exercicio_07"

var
peso, altura, IMC: real
inicio
escreva("Digite seu peso: ")
leia(peso)
escreva("Digite sua altura: ")
leia(altura)

IMC <- peso / (altura ^ 2)

escreva("Seu IMC é: ", IMC:4:2)
escreval("")

se IMC < 18.5 entao
escreval("Voce esta abaixo do peso")
senao
se (IMC >= 18.5) e (IMC < 25 ) entao
escreval("Voce esta com o peso normal")
senao
se (IMC >= 25) e (IMC < 30) entao
escreval("Voce esta sobrepeso")
senao
se (IMC <= 35) e (IMC < 40) entao
escreval("Voce é OBESO")
senao
escreval("VOCE È OBESO MORBIDO")
fimse
fimse
fimse
fimse
fimalgoritmo
