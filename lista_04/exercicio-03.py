distancia = int(input("Digite a distancia percorrida pelo carro (em km): "))
combustivel = int(input("Digite a quantidade de combustivel consumida (em litros): "))

if distancia > 0:
    media_consumo = (distancia / combustivel)
    print(f"Sua média de consumo foi de {media_consumo:.2f} Litros")
else:
    print("Nao foi possivel realizar a operação")
                        
