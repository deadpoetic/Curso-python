#Progressão Aritmética

p1 = int(input('Digite um número: '))
r = int(input('Digite a razão: '))
pa = 0
for c in range(2, 12):
    if c == 2:
       pa = p1
    else:
        pa = pa + r
    print(pa)