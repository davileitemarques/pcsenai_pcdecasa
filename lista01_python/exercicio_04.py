v_media = float(input("Digite o valor da velocidade media (em m/s): "))

if v_media != 0:
  conversao = v_media / 3.6
  print(f"O resultado da conversao é de {conversao:.2f} km/s")
else:
  print("Não foi possivel efetuar a conversão")

