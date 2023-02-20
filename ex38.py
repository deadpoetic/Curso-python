#Comparando números

num1 = int(input('Digite um numero: '))
num2 = int(input('Digite um numero: '))
if num1 > num2:
    print(f'O maior valor é {num1} ')
elif num2 > num1:
    print(f'O malor valor é {num2}')
else:
    print('Não existe valor maior, os dois são iguais')