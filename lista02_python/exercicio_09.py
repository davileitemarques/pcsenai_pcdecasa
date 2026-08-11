
inicial = float(input("Digite o deposito inicial na sua poupança: "))
mes = float(input("Digite o valor depositado mensalmente: "))
taxa = float(input("Digite a taxa de juros da poupança: "))

<<<<<<< HEAD
total = inicial
contador = True
saldo = inicial
decimal = taxa / 100
 
while True:
    saldo = saldo + mes
    total = total + mes 
=======
contador = 1
saldo = inicial
decimal = taxa / 100
 
while contador <= 24:
    saldo = saldo + mes 
>>>>>>> 8e75f6d1acebacdbe8f0001e91077a5806a159bd
    saldo = saldo + (saldo * decimal)
    print(f"Mes {contador} saldo: {saldo:.2f}")
    contador += 1

juros = saldo - inicial
print(f"O juros é de R${juros:.2f}")