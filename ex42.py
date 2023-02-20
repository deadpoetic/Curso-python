#Analisando Triângulos v2.0

r1 = float(input('Digite o primeiro comprimento '))
r2 = float(input('Digite o segundo comprimento '))
r3 = float(input('Digite o terceiro comprimento '))
tipo = 0
cond = 0
if r1 >= r2 and r1 >= r3 and r2 + r3 > r1:
    cond = 1
    print('Pode ser um triangulo')
elif r2 >= r1 and r2 >= r3 and r1 + r3 > r2:
    cond = 1
    print('Pode ser um triangulo')
elif r3 >= r1 and r3 >= r2 and r1 + r2 > r3:
    cond = 1
    print('Pode ser um triangulo')
else:
    print('Não pode ser um triangulo')
if r1 != r2 and r1 != r3 and r2 != r3 and cond == 1:
    tipo = 'Escaleno'
    print(f'Seu triângulo é um do tipo {tipo}')
elif r1 == r2 and r1 == r3 and r2 == r3 and cond == 1:
    tipo = 'Equilátero'
    print(f'Seu triângulo é um do tipo {tipo}')
elif r1 == r2 or r1 == r3 or r2 == r3 and cond ==1:
    tipo = 'Isósceles'
    print(f'Seu triângulo é um do tipo {tipo}')