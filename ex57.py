cond = 1
sexo = str(input('Digite o seu sexo: ')).upper()
if sexo == 'F' or sexo == 'M':
    cond = 0
while cond != 0:
    sexo = str(input('Opção invlálida, tente novamente.\nDigite o seu sexo: ')).upper()
    if sexo == 'F' or sexo == 'M':
        cond = 0
print('Fim')
