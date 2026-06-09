algoritmo "exercicio_01"

var
nota1, nota2, nota3, media: real
inicio
escreva("Sua primeira nota: ")
leia(nota1)
escreva("Sua segunda nota: ")
leia(nota2)
escreva("Sua terceira nota: ")
leia(nota3)

media <- nota1 + nota2 + nota3 / 3

se media >= 7 entao
escreva("Voce foi aprovado")
senao
escreva("Voce foi reprovado")
fimse
fimalgoritmo
