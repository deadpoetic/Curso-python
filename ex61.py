pt = int(input('Digite o primeiro termo: '))
raz = int(input('Digite a razão: '))
t = 0
nt = 1
while t < 10:
    t = t + 1
    if t == 1:
        nt = 1
        pt = pt
        print(f'{t}º termo = {pt}')
    else:
        nt = t
        pt = pt + raz
        print(f'{nt}º termo = {pt}')
