#Tabuada V3
while True:
    val = int(input('Digite um número para saber a sua tabuada: '))
    c = 0
    if val < 0:
        break
    while c < 10:
        c += 1
        resu = val * c
        print(f'{val} x {c} = {resu}')
print('Volte sempre.')