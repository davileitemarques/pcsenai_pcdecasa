#Peça os dois numeros ao usuario
n1 = float(input("Digite o seu numero: "))
n2 = float(input("Digite seu segundo numero: "))
#Soma entre os numeros
soma = n1 + n2
#Conferindo se é possivel efetuar a operaçao
if n1 != 0 and n2 != 0:
   produto = n1 * n2
#Se for possivel, imprima normalmente
   print(f"O valor da soma é {soma} e o valor do produto é {produto}")
else:
#Senao, imprima apenas a soma
   print("Não foi possivel efetuar a operação do produto")
   print(f"O resultado da soma é {soma}")