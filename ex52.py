#Números primos

num = int(input('Digite um numero: '))
cont = 0
for c in range(1, num + 1):
    if num % c == 0:
        cont = cont + 1
        if cont == 2:
            print('Este é um número primo.')
            break
else:
    print('Este não é um número primo')