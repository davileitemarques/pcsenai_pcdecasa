
horas_trabalhadas = int(input("Digite a quantidade de horas trabalhadas no mes: "))
salario_hora = float(input("Digite o salario por horas trabalhadas: "))

if horas_trabalhadas > 160:
    horas_extras = (horas_trabalhadas - 160)
    salario_total = (salario_hora * 160) + (horas_extras * salario_hora * 1.50)
else:
    salario_total = (salario_hora * horas_trabalhadas)
print(f"Seu salario total é de: R${salario_total:.2f}")