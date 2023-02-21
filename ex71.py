#Simulador de caixa eletrônico
c = 50
v = 20
d = 10
u = 1
s = c1 = v1 = d1 = u1 = 0
num = int(input('Qual o valor deseja sacar? '))
while s < num:
    s += c
    c1 += 1
    resp = f'{c1} Cédulas de R${c}'
    print(s)
if s > num:
    s = s - c
    c1 += - 1
    while s < num:
        s += v
        v1 += 1
        resp = f'{c1} Cédulas de R${c}\n{v1} Cédulas de R${v}\n'
    if s > num:
        s += - v
        v1 += -1
        while s < num:
            s += d
            d1 += 1
            resp = f'{c1} Cédulas de R${c}\n{v1} Cédulas de R${v}\n{d1} Cédulas de R${d}'
        if s > num:
            s += - d
            d1 += -1
            while s < num:
                s += u
                u1 += 1
                resp = f'{c1} Cédulas de R${c}\n{v1} Cédulas de R${v}\n{d1} Cédulas de R${d}\n{u1} Cédulas de R${u}'
print(resp)