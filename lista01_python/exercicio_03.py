n1 = float(input("Digite o seu numero: "))
n2 = float(input("Digite seu segundo numero: "))

soma = n1 + n2

if n1 != 0 and n2 != 0:
   produto = n1 * n2
   print(f"O valor da soma é {soma} e o valor do produto é {produto}")
else:
   print("Não foi possivel efetuar a operação do produto")
   print(f"O resultado da soma é {soma}")