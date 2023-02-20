#Maior e menor valores

n1 = int(input('Digite o primeiro numero: '))
n2 = int(input('Digite o segundo numero: '))
n3 = int(input('Digite o terceiro numero: '))
if n1 >= n2 and n1 >= n3 and n2 >= n3:
    maior = n1
    menor = n3
elif n1 >= n2 and n1 >= n3 and n2 < n3:
    maior = n1
    menor = n2
if n2 >= n1 and n2 >=n3 and n1 >= n3:
    maior = n2
    menor = n3
elif n2 >= n1 and n2 >= n3 and n1 < n3:
    maior = n2
    menor = n1
if n3 >= n1 and n3 >= n2 and n1 >= n2:
    maior = n3
    menor = n2
elif n3 >= n1 and n3 >= n2 and n1 < n2:
    maior = n3
    menor = n1
print(f'1-Maior numero {maior}\n1-Menor numero {menor}')