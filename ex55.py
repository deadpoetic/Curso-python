#Maior e menor da sequência

lista = []
for c in range(1, 6):
    pes = int(input('Digite o seu peso: '))
    lista.append(pes)
print(f'Maior peso: {max(lista)}\nMenor peso: {min(lista)}')



#ou

pes = int(input('Digite o 1º Peso: '))
maipes = pes
menpes = pes
for c in range(2, 7):
    pes = int(input(f'Digite o {c}º Peso: '))
    if pes > maipes:
        maipes = pes
    if pes < menpes:
        menpes = pes
print(maipes, menpes)