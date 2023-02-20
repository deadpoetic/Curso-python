#GAME: Pedra Papel e Tesoura

import random
jog = int(input('Escolha\n1-Pedra\n2-Papel\n3-Tesoura\n: '))
n1 = 'Pedra'
n2 = 'Papel'
n3 = 'Tesoura'
if jog == 1:
    esc = 'Pedra'
elif jog == 2:
    esc = 'Papel'
else:
    esc = 'Tesoura'
lista = [n1, n2, n3]
pc = random.choice(lista)
print(f'Eu escolhi {pc} e você {esc}.')
#perder
if jog == 1 and pc == n2 or jog == 2 and pc == n3 or jog == 3 and pc == n1:
    print(f'{pc} ganha de {esc}\nVocê perdeu.')
#ganhar
elif jog == 1 and pc == n3 or jog == 2 and pc == n1 or jog == 3 and pc == n2:
    print(f'{esc} ganha de {pc}\nVocê ganhou.')
else:
    print('Empatou.')

#PEDRA, PAPEL E TESOURA V2

import random
from time import sleep
def menu():
    print('\33[0:31m=\33[m' * 15)
    print('[ 1 ] Pedra\n[ 2 ] Papel\n[ 3 ] Tesoura\n[ 4 ] Sair')
    print('\33[0:31m=\033[m' * 15)

def anima():
    print('\033[0:33m+-' * 10 + '+')
    print('\33[0:31mJO')
    sleep(0.8)
    print('\33[0:32mKEN'.center(25))
    sleep(0.8)
    print('\33[0:34mPO'.center(45))
    print('\033[0:33m+-' * 10 + '+\033[m')

def start():
    pc = jog = vitoria = derrota = c = eu = empate = vitn = dern = empn = 0
    while True:
        lista = ['Pedra', 'Papel', 'Tesoura']
        pc = random.choice(lista)
        menu()
        jog = int(input('Opção: '))
        if jog > 4:
            print('Opção inválida, digite novamente.')
        if jog == 1:
            eu = 'Pedra'
            c += 1
        if jog == 2:
            eu = 'Papel'
            c += 1
        if jog == 3:
            eu = 'Tesoura'
            c += 1
        if jog == 4:
            c += 1
            if c == 1:
                print('Volte Sempre.')
            else:
                print(f'Você ganhou {vitoria} {vitn}.\nEu ganhei {derrota} {dern}.\nEmpatamos {empate} {empn}.')
            break
        if jog == 1 and pc == 'Papel' or jog == 2 and pc == 'Tesoura' or jog == 3 and pc == 'Pedra':
            anima()
            sleep(1)
            derrota += 1
            print('*' * 20, ' ' * 20, '*' * 22)
            print(f'Eu escolhi {pc}.'.center(20), ' ' * 20, f'Você escolheu {eu}.'.center(22))
            print('*' * 20, ' ' * 20, '*' * 22)
            sleep(0.5)
            print(' ' * 23, '*' * 14)
            print('Eu ganhei!!!'.center(62))
            print(' ' * 23, '*' * 14)
        elif jog == 1 and pc == 'Tesoura' or jog == 2 and pc == 'Pedra' or jog == 3 and pc == 'Papel':
            vitoria += 1
            anima()
            sleep(1)
            print('*' * 20, ' ' * 20, '*' * 22)
            print(f'Eu escolhi {pc}.'.center(20), ' ' * 20, f'Você escolheu {eu}.'.center(22))
            print('*' * 20, ' ' * 20, '*' * 22)
            sleep(0.5)
            print(' ' * 23, '*' * 14)
            print('Você ganhou!!!'.center(62))
            print(' ' * 23, '*' * 14)
        elif jog == 1 and pc == 'Pedra' or jog == 2 and pc == 'Papel' or jog == 3 and pc == 'Tesoura':
            empate += 1
            anima()
            sleep(1)
            print('*' * 20, ' ' * 20, '*' * 22)
            print(f'Eu escolhi {pc}.'.center(20), ' ' * 20, f'Você escolheu {eu}.'.center(22))
            print('*' * 20, ' ' * 20, '*' * 22)
            sleep(0.5)
            print(' ' * 23, '*' * 14)
            print('Empatamos!!!'.center(62))
            print(' ' * 23, '*' * 14)
        if vitoria == 1:
            vitn = 'Vez'
        else:
            vitn = 'Vezes'
        if derrota == 1:
            dern = 'Vez'
        else:
            dern = 'Vezes'
        if empate == 1:
            empn = 'Vez'
        else:
            empn = 'Vezes'

start()