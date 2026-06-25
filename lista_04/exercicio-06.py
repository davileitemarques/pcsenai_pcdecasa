
homem1 = int(input("Digite a idade do primeiro homem: "))
homem2 = int(input("Digite a idade do segundo homem: "))
mulher1 = int(input("Digite a idade da primeira mulher: "))
mulher2 = int(input("Digite a idade da segunda mulher: "))

if (homem1 != homem2) and (mulher1 != mulher2):
   if (homem1 > homem2) and (mulher1 > mulher2):
    soma = homem1 + mulher2
    produto = homem2 * mulher1
   elif (homem2 > homem1) and (mulher1 > mulher2):
    soma = homem2 + mulher2
    produto = homem1 * mulher1
   elif (homem2 > homem1) and (mulher2 > mulher1):
    soma = homem2 + mulher1
    produto = homem1 * mulher2
   elif (homem1 > homem2) and (mulher2 >mulher1):
    soma = homem1 + mulher1
    produto = homem2 * mulher2   
#Lembrar de sempre colocar o print atribuido a uma variavel criada dentro de uma outra condicional, dentro do bloco dessa outra condicional, senao a variavel nao é reconhecida.
   print(f"A soma das idades do homem mais velho e a mulher mais nova é: {soma}")
   print(f"O produto das idades do homem mais novo e a mulher mais velha é: {produto}")
else:
   print("Não foi possivel efetuar as operações (idades iguais)")