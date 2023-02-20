#Grupo da Maioridade


import datetime
data = datetime.date.today().year
ano = 0
maior = 0
menor = 0
for c in range(1, 8):
    ano = int(input(f'Digite a {c}º data: '))
    idade = data - ano
    if idade >= 18:
        maior = maior + 1
    else:
        menor = menor + 1
print(f'{maior} Pessoas são de maior\n{menor} Pessoas são de menor.')