#Número por extenso

num = ('Zero', 'Um', 'Dois', 'Tres', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
while True:
    numinpt = int(input('Digite um número de 0 a 20: '))
    if numinpt > 20 or numinpt < 0:
        print('Numéro inválido, tente novamente.')
    else:
        break
print(f'Você digitou o número {num[numinpt]}')