#Simulador de caixa eletronico v2 kappa
s = c1 = v1 = d1 = u1 = resp = 0
num = int(input('Qual o valor deseja sacar? '))
while 50 <= num:
    num -= 50
    c1 += 1
    resp = (f'{c1} Cédulas de R$50')
if c1 >= 1:
    print(resp)
while 20 <= num:
    num -= 20
    v1 += 1
    resp = (f'{v1} Cédulas de R$20')
if v1 >= 1:
    print(resp)
while 10 <= num:
    num -= 10
    d1 += 1
    resp = (f'{d1} Cédulas de R$10')
if d1 >= 1:
    print(resp)
while 1 <= num:
    num -= 1
    u1 += 1
    resp = (f'{u1} Cédulas de R$1')
if u1 >= 1:
    print(resp)


import math
#Simulador de caixa eletrônico #Bruno
lista = [50, 20, 10, 1]
num = int(input('Qual o valor deseja sacar? '))
for valor_cedula in lista:
    total_cedula = math.floor(num / valor_cedula)
    print(num)
    num = num - total_cedula * valor_cedula
    if total_cedula > 0:
        print(f'{total_cedula},de R${valor_cedula}')

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
