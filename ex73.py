#Tuplas com times de futebol

tabela_bras_a = ('América-MG', 'Athletico-PR', 'Atlético-MG', 'Bahia', 'Botafogo', 'Corinthians', 'Coritiba', 'Cruzeiro', 'Cuiabá', 'Flamengo', 'Fluminense', 'Fortaleza', 'Goiás', 'Grêmio', 'Internacional', 'Palmeiras', 'Bragantino', 'Santos', 'São Paulo', 'Vasco da Gama')
print('Cinco primeiros colocados da tabela:')
for c in range(0, 5):
    print(f'{c + 1}º {tabela_bras_a[c]}')
print('Quatro últimos colocados da tabela.')

for ultimos in (tabela_bras_a[-4:]):
    count = tabela_bras_a.index(ultimos) + 1
    print(f'{count}º {ultimos}')
print(f'Tabela em ordem alfabética\n{sorted(tabela_bras_a)}')

for pos, n in enumerate(tabela_bras_a):
    if n == 'Bahia':
        print(f'O time {n} está em {pos + 1}º Lugar')




