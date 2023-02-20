#Sorteando um item na lista
import random
a1 = str(input('Nome do primeiro aluno '))
a2 = str(input('Nome do segundo aluno'))
a3 = str(input('Nome do terceiro aluno'))
a4 = str(input('Nome do quarto aluno'))
e = [a1, a2, a3, a4]
print(f'{a1}, {a2}, {a3}, {a4}.\n{random.choice(e)} foi escolhido para apagar o quadro.')