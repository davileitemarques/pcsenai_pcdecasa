
c_empregado = int(input("Digite o seu codigo de empregado: "))
ano_nasc = int(input("Digite o seu ano de nascimento: "))
ingresso = int(input("Digite o seu ano de ingresso na empresa: "))

ano_atual = 2026
idade = ano_atual - ano_nasc
tempo_trabalhado = ano_atual - ingresso

print(f"Seu codigo: {c_empregado}")
print(f"Sua idade é: {idade} anos")
print(f"Seu tempo na empresa é de: {tempo_trabalhado} anos")

if idade >= 65 or tempo_trabalhado >= 30 or (idade >= 60 and tempo_trabalhado >= 25):
    print("Requerer aposentadoria!!")
else:
    print("Não requerer aposentadoria!!")