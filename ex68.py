#Jogo do par ou impar

import random
vit = 0
print('Vamos jogar par ou impar.')
while True:
    num = int(input('Digite um número: '))
    esc = int(input('Digite\n1-Par\n2-Impar\n:'))
    if esc == 1:
        esc1 = 'Par'
    else:
        esc1 = 'Impar'
    numpc = random.randint(0, 5)
    soma = num + numpc
    #if soma % 2 == 0:
    pi = 'Par' if soma % 2 == 0 else 'Impar'
    #else:
        #pi = 'Impar'
    print(f'Você digitou o número {num} e escolheu {esc1}\nEu escolhi o número {numpc}\n{num} + {numpc} é {pi}')
    if esc == 1 and soma % 2 != 0 or esc == 2 and soma % 2 == 0:
        print('Você perdeu.')
        break
    vit += 1
    print('Você ganhou, vamos jogar novamente!')
print(f'Você ganhou {vit} vezes.')
