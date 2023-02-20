#Índice de Massa Corporal

peso = float(input('Digite o seu peso: '))
altura = float(input('Digite a sua altura: '))
imc = peso / (altura * altura)
print(imc)
if imc < 18.5:
    print('Você está abaixo do peso.')
elif imc <= 24:
    print('Você está no peso ideal.')
elif imc <= 29:
    print('Você está com sobrepeso.')
elif imc <= 39:
    print('Você está com obesidade.')
else:
    print('Você está com obesidade mórbida.')