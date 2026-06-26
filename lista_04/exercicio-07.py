
quant_maca = int(input("Digite a quantidade de maçãs (em kg): "))
quant_morango = int(input("Digite a quantidade de morangos (em kg): "))

if quant_maca <= 5:
    preco = 1.80
    valor_total_maca = (quant_maca * 1.80)
else:
     preco = 1.50
     valor_total_maca = (quant_maca * 1.50)

valor_final_maca = valor_total_maca


if quant_morango <= 5:
    preco = 2.50
    valor_total_morango = (quant_morango * 2.50)
else:
    preco = 2.20
    valor_total_morango = (quant_morango * 2.20)

valor_final_morango = valor_total_morango


if (quant_morango > 8) or (valor_total_morango > 25) and (quant_morango > 8) or (valor_total_maca > 25):
 valor_final = (valor_final_maca + valor_total_morango) * 0.90

print(f"O valor final a ser pago é de: R${valor_final:.2f}")