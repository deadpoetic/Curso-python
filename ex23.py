#Separando dígitos de um número

numero = input('Digite um numero: ')
mil = numero[0]
cent = numero[1]
dez = numero[2]
uni = numero[3]
print(f'Unidade {uni}, dezena {dez}, centena {cent}, milhar {mil}')