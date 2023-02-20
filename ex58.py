import random
cont = 1
print('Tente adivinha o número que eu pensei de 0 a 10.')
num = int(input('Digite um número: '))
pc = random.randint(0, 2)
while num != pc:
    print(f'Você errou!\nEu escolhi {pc} e você escolheu {num}.\nTente novamente.')
    num = int(input('Digite um número de 0 a 10: '))
    pc = random.randint(0, 2)
    cont = cont + 1
print(f'Você acertou!!\nEu escolhi {pc} e você escolheu {num}.\nForam necessárias {cont} tentativas para acertar.')


