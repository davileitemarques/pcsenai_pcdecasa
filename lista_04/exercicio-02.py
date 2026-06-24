
quantidade_atual = int(input("Digite a quantidade atual em estoque: "))
quantidade_minima = int(input("Digite a quantidade minima em estoque: "))
quantidade_maxima = int(input("Digite a quantidade maxima em estoque: "))

quantidade_media = (quantidade_minima + quantidade_maxima / 2)

if quantidade_atual >= quantidade_media:
    print("Nao efetuar a compra!")
else:
    print("Efetuar a compra")
    