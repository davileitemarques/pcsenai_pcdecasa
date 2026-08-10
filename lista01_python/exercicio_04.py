#Pergunte a velocidade media ao usuario
v_media = float(input("Digite o valor da velocidade media (em m/s): "))
#Conferindo se é possivel fazer a conversão
if v_media != 0:
  conversao = v_media / 3.6
#Se sim, imprima o resultado normalmente
  print(f"O resultado da conversao é de {conversao:.2f} km/s")
else:
#Se nao, imprima que nao foi possivel efetuar a operação
  print("Não foi possivel efetuar a conversão")

