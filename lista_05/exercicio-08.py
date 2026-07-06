
nome_vencedoras = []
maior_nota = None

for i in range(1, 17):
    print(f"Candidata numero {i}")
    nome = str(input("Digite o nome da candidata: "))
    nota = int(input("Digite a nota da candidata (0 a 10): "))
    if maior_nota is None or nota > maior_nota:
        nome_vencedoras = [nome]
        maior_nota = nota
    elif nota == maior_nota or nota == maior_nota:
        nome_vencedoras.append(f"{nome}")

print(f"A maior nota foi {maior_nota}") 
print(f"A(s) candidata(s) campeã(s) são: {', '.join(nome_vencedoras)}")