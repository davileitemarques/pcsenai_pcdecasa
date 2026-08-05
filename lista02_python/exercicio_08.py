
total = 0

inicial = float(input("Digite o deposito inicial na sua poupança: "))
taxa = float(input("Digite a taxa de juros da poupança: "))

for i in range(1, 25):
    print(f"MES {i}")
    inicial += (1 + taxa / 100)
    print(f"O valor total desse mes é de R${inicial}")