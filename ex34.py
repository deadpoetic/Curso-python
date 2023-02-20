#Aumentos múltiplos

salario = int(input('Quanto você ganha? '))
bonus = 0
if salario > 1250:
    bonus = salario * 1.10
else:
    bonus = salario * 1.15
print(f'O seu novo salário com a bonificação é de {bonus} ')