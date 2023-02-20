#Sequência de Fibonacci v1.0

num = int(input('Digite um número: '))
t = 0
ultimo = 1
penultimo = 1
val = 0
while t < num:
    t = t + 1
    if t == 1 or t == 2:
        val = 1
        print(val)
    else:
        val = ultimo + penultimo
        print(val)
        penultimo = ultimo
        ultimo = val
