#Detector de Palíndromo

n1 = str(input('Digite uma palavra: ')).strip()
n2 = n1.replace(' ','')
n3 = n2[::-1]
for c in range(0, len(n2)):
    if n2[c] != n3[c]:
        resp = ('Essa palavra NÃO é um palíndromo.')
        break
    else:
        resp = ('Essa palavra É um palíndromo.')
        break
print(f'O inverso de {n2} é {n3}\n{resp}')