#Pedindo a velociddde atingida pelo carro
velocidade = float(input("Digite a velocidade atingida pelo seu carro: "))
#Colocando as condicionais necessarias e criando novas variaveis
if velocidade > 80:
    excesso = velocidade - 80
    multa = excesso * 50
#Imprimindo o valor da multa
    print(f"Voce foi multado em um valor de R${multa}")
else:
#Se nao, imprimindo que o usuario atingiu uma velocidade permitida
    print("Velocidade permitida!!")
