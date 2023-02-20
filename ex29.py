#Radar eletrônico

velo = int(input('Digite a velocidade do carro: '))
preço = (velo - 80) * 7
if velo > 80:
    print(f'Você foi multado, você deverá pagar R${preço} de multa.')
else:
    print('Você não foi multado, tenha um bom dia.')