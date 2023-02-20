#Custo da Viagem

dist = float(input('Digite quantos KM foram percorridos: '))
if dist <= 200:
    valor = dist * 0.5
    print(f'Valor a se pagar {valor}.')
else:
    valor = dist * 0.45
    print(f'Valor a se pagar {valor}.')