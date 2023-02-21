# Vários números com flag

c = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    c += 1
    soma += num
print(f'Você digitou {c} números e a soma entre eles é {soma}')