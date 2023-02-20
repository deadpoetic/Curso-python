#Aluguel de Carros
km = int(input('Quantos km o carro percorreu? '))
dias = int(input('Por quantos dias?'))
v1 = dias * 60
v2 = km * 0.15
valor = v1 + v2
print(f'O valor total a se pagar é {valor:.2f}')