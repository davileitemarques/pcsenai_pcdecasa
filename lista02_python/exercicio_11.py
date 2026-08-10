sonumeros = None

while True:
    cpf = input("Digite seu cpf contendo exatamente 11 digitos (sem pontos e tracos): ")
    if len(cpf) == 11:
        sonumeros = True
        for caractere in cpf:
            if caractere not in "0123456789":
                sonumeros = False
    if sonumeros == True:
        break
    else:
        print("Digite os 11 numeros do CPF (sem pontos ou traços)")
         
primeirocima = (int(cpf[0])) * 10
segundocima = (int(cpf[1])) * 9
terceirocima = (int(cpf[2])) * 8
quartocima = (int(cpf[3])) * 7
quintocima = (int(cpf[4])) * 6
sextocima = (int(cpf[5])) * 5
setimocima = (int(cpf[6])) * 4
oitavocima = (int(cpf[7])) * 3
nonocima = (int(cpf[8])) * 2

soma1 = primeirocima + segundocima + terceirocima + quartocima + quintocima + sextocima + setimocima + oitavocima + nonocima
divisao1 = soma1 // 11
multiplica1 = divisao1 * 11
subtracao1 = soma1 - multiplica1
if (subtracao1 == 1) or (subtracao1 == 0):
    digito1 = 0
else:
    digito1 = 11 - subtracao1

primeirobaixo = (int(cpf[0])) * 11
segundobaixo = (int(cpf[1])) * 10
terceirobaixo = (int(cpf[2])) * 9
quartobaixo = (int(cpf[3])) * 8
quintobaixo = (int(cpf[4])) * 7
sextobaixo = (int(cpf[5])) * 6
setimobaixo = (int(cpf[6])) * 5
oitavobaixo = (int(cpf[7])) * 4
nonobaixo = (int(cpf[8])) * 3
decimobaixo = (int(cpf[9])) * 2

soma2 = primeirobaixo + segundobaixo + terceirobaixo + quartobaixo + quintobaixo + sextobaixo + setimobaixo + oitavobaixo + nonobaixo + decimobaixo
divisao2 = soma2 // 11
multiplica2 = divisao2 * 11
subtracao2 = soma2 - multiplica2
if (subtracao2 == 1) or (subtracao2 == 0):
    digito2 = 0
else:
    digito2 = 11 - subtracao2

if (digito1 == int(cpf[9])) and (digito2 == int(cpf[10])):
    print("Seu CPF é valido")
else:
    print("Seu CPF é invalido")