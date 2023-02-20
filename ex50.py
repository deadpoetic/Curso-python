#Soma dos pares
#1º forma
lista = []
resp = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º numero: '))
    if num % 2 == 0:
        par = num
        lista.append(par)
        soma = sum(lista)
print(soma)
#2º forma
soma = 0
cont = 0
for c in range(1, 7):
    num = int(input(f'Digite o {c}º número: '))
    if num % 2 == 0:
        soma += num
        cont += 1
print(f'Você digitou {cont} pares e a soma deles é igual a {soma}.')