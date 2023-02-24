#Analise de dados em uma tupla
listar_num = ''
tupla = ()
listar_par = ''
quant_nove = pos_3 = cond_par = cond_3 = cond_9 = par = num_3 = 0
for c in range(0, 4):
    num = int(input(f'Digite o {c + 1}º número: '))
    listar_num += f'{str(num)} '
    tupla += (num,)
    cond_9 = f'O número 9 foi digitado {tupla.count(9)} vezes'
    if num % 2 == 0:
        listar_par += f'{str(num)} '
        cond_par = f'Os valores pares digitados foram: {listar_par}'
        par += 1
    if par == 0:
        cond_par = 'Não existem números pares dentre os valores digitados.'
if 3 in tupla:
    pos_3 = tupla.index(3)
    cond_3 = f'O primeiro número 3 está na {pos_3 + 1}ª posição.'
    num_3 += 1
else:
    cond_3 = 'O valor 3 não foi digitado.'
print(f'Você digitou os valores: {listar_num}')
print(f'{cond_9}.\n{cond_par}\n{cond_3}')