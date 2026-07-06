
v1 = float(input("Digite o primeiro valor: "))
v2 = float(input("Digite o segundo valor: "))
#O while é diferente do If pois o if pula esse processo a partir do momento em q ele nao é verdadeiro, o while nao, ele volta
while v2 == 0:
    print("Não foi possivel fazer a operação, digite outro valor")
    v2 = float(input("Digite o segundo valor: "))

resultado = v1 / v2

print(f"O resultado da divisão entre os dois valores é: {resultado:.2f}")