#Primeiro e último nome de uma pessoa

nome = str(input('Digite o seu nome: '))
lista = nome.split()
primeiro = lista[0]
ultimo = lista[-1]
print(f'Primeiro nome: {primeiro.upper()}\nUltimo nome: {ultimo.upper()}')