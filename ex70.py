#Estatisticas em produtos

soma = p = 0
c = 1
nom = str(input(f'Digite o nome do 1º produto: ')).capitalize()
preço1 = float(input(f'Digite o preço do 1º produto: '))
barato = preço1
maisb = nom
if preço1 > 1000:
    c = 1
while True:
    c += 1
    cont = 0
    while cont != 'S' and cont != 'N':
        cont = str(input('Quer continuar? [S/N]: ')).upper()
    if cont == 'N':
        break
    nom = str(input(f'Digite o nome do {c}º produto: ')).capitalize()
    preço = float(input(f'Digite o preço do {c}º produto: '))
    soma += preço
    if preço > 1000:
        p += 1
    if preço < barato:
        barato = preço
        maisb = nom
print(f'O valor total dos produtos é R${soma + preço1:.2f}\n{p} Produtos custam mais que R$1000.00\nO Produto mais barato foi {maisb} que custa R${barato:.2f}')