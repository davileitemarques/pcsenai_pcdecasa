valor_casa = float(input("Digite o valor da casa à comprar: "))
s = float(input("Digite o valor do seu salario mensal: "))
anos = int(input("DIgite a quantidade de anos que voce vai pagar a casa: "))

meses = anos * 12
prestacao = valor_casa / meses

if prestacao > s * 0.30:
    print("Não foi possivel efetuar a compra da casa")
else:
    print(f"O valor das prestações mensais a pagar é de R${prestacao:.2f}")
