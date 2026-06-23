algoritmo "exercicio04"


var
branco, nulos, valido, eleitores: inteiro
 percbran, percvalido, percnulos: real
inicio
escreva("Total de eleitores do municipio: ")
leia(eleitores)
escreva("Total de votos validos: ")
leia(valido)
escreva("Total de votos nulos: ")
leia(nulos)
escreva("Total de votos em branco: ")
leia(branco)

percbran <- (branco / eleitores) * 100
percvalido <- (valido / eleitores) * 100
percnulos <- (nulos / eleitores) * 100

escreval("O percentual de votos em branco é: ", percbran:2:2, "%")
escreval("O percentual de votos valios é: ", percvalido:2:2, "%")
escreval("O percentual de votos nulos é: ", percnulos:2:2, "%")
fimalgoritmo
