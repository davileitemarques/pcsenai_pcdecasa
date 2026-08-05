kwh = float(input("Digite a quantidade de kilowatts consumida: "))
instalacao = str(input("Digite o tipo de instalação (R-Residencial, I-Industrial e C-Comercial): ")).upper()

while instalacao not in ["R", "I", "C"]:
 print("Digite um tipo valido de instalação")
 instalacao = str(input("Digite o tipo de instalação (R-Residencial, I-Industrial e C-Comercial): ")).upper()

if instalacao == "R":
    if kwh <= 500:
        totalkwh = kwh * 0.40
    else:
        totalkwh = kwh * 0.65
    print(f"O total a pagar pelo consumo de KWH nesse mes é de R${totalkwh:.2f}")

elif instalacao == "I":
    if kwh <= 5000:
        totalkwh = kwh * 0.55
    else:
        totalkwh = kwh * 0.60
    print(f"O total a se pagar pelo consumo de KWH nesse mes é de R${totalkwh:.2f}")

elif instalacao == "C":
    if kwh <= 1000:
        totalkwh = kwh * 0.55
    else:
        totalkwh = kwh * 0.60
    print(f"O total a se pagar pelo consumo de KWH nesse mes é de R${totalkwh:.2f}")