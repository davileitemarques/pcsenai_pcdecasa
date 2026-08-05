
adicao = 0
quantidade = 0

while True:
    num = int(input("Digite um numero inteiro (ou 0 para sair): "))
    if num == 0:
        print("Saida efetuada com sucesso")
        break
    adicao = adicao + num
    quantidade += 1
    if quantidade > 0:
         media = adicao / quantidade
         print(f"A soma é {adicao}")
         print(f"A quantidade de numeros digitados são {quantidade}")
         print(f"A media é {media}")