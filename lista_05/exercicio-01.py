
nome_produto = str(input("Digite a descrição do produto (nome): "))
quantidade_adquirida = int(input("Digite a quantidade de produtos aquiridos: "))
preco_unitario = float(input("Digite o preço pago por produto: "))

total = quantidade_adquirida * preco_unitario

if quantidade_adquirida <= 5:
    total_d = total * 0.98
elif quantidade_adquirida <= 10:
    total_d = total * 0.97
else:
    total_d = total * 0.95

if quantidade_adquirida and preco_unitario > 0:
 print(f"O valor total a ser pago é de: R${total_d:.2f}")
else:
   print("Não foi possivel efetuar a operação")