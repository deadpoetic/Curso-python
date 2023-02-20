num = 0
soma = 0
quant = 0
ult = 0
while num != 999:
    num = int(input('Digite um número: '))
    quant = quant + 1
    soma = soma + num
    if num == 999:
        soma = soma - 999
print(f'{quant} {soma}')