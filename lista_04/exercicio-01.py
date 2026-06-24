
numero_conta = int(input("Digite o numero da sua conta: "))
saldo = float(input("Digite o seu saldo atual: "))
debito = float(input("Digite o seu débito: "))
credito = float(input("Digite o seu crédito; "))

saldo_atual = (saldo - debito + credito)

if saldo_atual >= 0:
    print(f"R${saldo_atual} Saldo positivo!!!")
else:
    print(f"R${saldo_atual} Saldo negativo!!!")