#Tratando vários valores v1.0

num = 0
soma = 0
quant = 0
ult = 0
while num != 999:
    num = int(input('Digite um número: '))
    quant = quant + 1
    soma = soma + num
    if num == 999:
        soma = soma - num
        quant = quant - 1
print(f'Você digitou {quant} Números e a soma entre eles é {soma}.')