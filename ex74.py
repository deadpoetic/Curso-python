#Maior e menor valores em tupla

from random import randint
import sys
tupla = ''
menor = sys.maxsize
maior = 0
for c in range(0, 6):
    num = randint(0, 99)
    tupla += f'{str(num)} '
    if num > maior:
        maior = num
    if num < menor:
        menor = num
print(f'Os valores sorteados foram: {tupla}')
print(f'Maior número: {maior}\nMenor número: {menor}')
