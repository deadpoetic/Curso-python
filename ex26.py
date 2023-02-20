#Primeira e última ocorrência de uma string
frase = str(input('Digite uma frase: '))
quantosa = frase.count('a')
primeiro = frase.find('a')
ultimo = frase.rfind('a')
print(f'Número de letras a {quantosa}\nPosição da primeira letra a {primeiro}\nÚltima letra a {ultimo}')