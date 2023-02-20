soma = num = res = med = 0
c = c1 = 1
num1 = int(input('Digite um número: '))
maior = num1
menor = num1
while True:
    resp = str(input('Quer continuar? S/N: ')).upper()
    c = c + 1
    if resp == 'N' and c == 2:
        res = 'Você só digitou um número.'
    if c == 3 and num == num1:
        res = 'Os dois valores são iguais'
    if resp == 'S':
        num = int(input('Digite um número: '))
        soma = soma + num
        med = soma + num1
    if resp == 'N':
        break
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    res = (f'Maior número: {maior}\nMenor número: {menor}\nMédia: {med / c}')
    if num == num1:
        c1 = c1 + 1
        if c == c1:
            res = 'Todos os valores são iguais'
print(c, res)

'''num = int(input('Digite um valor '))
maior = num
menor = num5
for c in range(5):
    num = int(input('Digite um valor'))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(maior, menor)'''
