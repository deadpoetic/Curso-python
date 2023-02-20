#Cálculo do Fatorial

num = int(input('Digite um número para saber o seu fatorial: '))
c = 1
result = 1
while c <= num:
    result = result * c
    c = c + 1
print(result)
