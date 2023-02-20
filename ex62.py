#Super Progressão Aritmética v3.0

pt = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
numt = int(input('Digite o número de termos a ser mostrado: '))
if numt != 0:
    t = 0
    while t < numt:
        t = t + 1
        if t == 1:
            pt = pt
            print(pt)
        else:
            pt = pt + raz
            print(pt)
else:
    print('Fim')