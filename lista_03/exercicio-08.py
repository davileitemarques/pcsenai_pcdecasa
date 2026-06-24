
maca_base = int(input("Quantidade de maçãs compradas: "))
if maca_base < 12:
    preco = maca_base * 1.30
    print(f"O preco total é R${preco:.2f}")
else:
    preco = maca_base * 1
    print(f"O preco total é R${preco:.2f}")
    