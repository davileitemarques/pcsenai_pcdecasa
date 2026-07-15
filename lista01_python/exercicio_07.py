
nome = str(input("Digite o nome do corretor: "))
quant_imoveis = int(input("Digite a quantidade de imóveis vendidos: "))
valortotal = float(input("Digite o valor final de suas vendas: "))

s_base = 2.500
comissao = (200 * quant_imoveis) + (0.05 * valortotal)
s_final = s_base + comissao

print(f"O salario final do corretor é de : R${s_final}")