#Analise de dados do grupo

c = i = h = m = 0
print('Cadastre uma pessoa.')
while True:
    c += 1
    idade = int(input(f'Digite a idade da {c}º Pessoa: '))
    cont = sexo = 0
    while sexo != 'M' and sexo != 'F':
        sexo = str(input(f'Digite o sexo da {c}º Pessoa[M/F]: ')).upper()
    while cont != 'S' and cont != 'N':
        cont = str(input('Quer continur?[S/N]: ')).upper()
    if idade > 18:
        i += 1
    if sexo == 'M':
        h += 1
    if sexo == 'F' and idade < 20:
        m += 1
    if cont == 'N':
        break
print(f'{i} Pessos tem mais de 18 anos, Dentre eles {m} Mulheres tem menos de 20 anos e ao todo {h} Homens foram cadastrados.')