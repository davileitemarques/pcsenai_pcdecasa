
litros_vendidos = float(input("Digite a quantidade de litros vendidos: "))
#Colocar o .upper() para evitar erro de digitação do usuario
tipo = str(input("Digite o tipo de combustivel (A-a para Alcool e G-g para Gasolina): ")).upper()

#If principal, para condicionar se for Gasolina
if tipo == "G":
   preco = 6.30
#Pergunta dos litros SÓ para a gasolina, o if é usado pois queremos colocar uma condicional dentro de outra, o elif nao é usado nesses casos, apenas quando for diferente ou o contrario
   if (litros_vendidos <= 20):
    desconto = (litros_vendidos * preco) * (1 - 0.04)
#Este else debaixo é para o If com espacamento p/direita, tanto que ele tambem esta para a direita
   else:
    desconto = (litros_vendidos * preco) * (1 - 0.06)
#Este elif é um SENAOSE para o If principal, o elif foi usado pois se fosse o else, qlqr outra coisa seria Alcool
elif tipo == "A":
   preco = 3.90
   if (litros_vendidos <= 20):
    desconto = (litros_vendidos * preco) * (1 - 0.03)
   else:
     desconto = (litros_vendidos * preco) * (1 - 0.05)
#Este else é do If principal, ele é acionado se nem o Alcool e nem a Gasolina fossem acionadas, sendo assim, um tipo invalido
else:
   print("Tipo de combustivel invalido")
#Ultimo checkout antes de finalizar o programa, se for diferente de 0 entao é verdadeiro
if desconto > 0:
   print(f"O valor total a ser pago é de: R${desconto:.2f}")