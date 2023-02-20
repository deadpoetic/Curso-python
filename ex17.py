#Catetos e Hipotenusa
from math import sqrt
co = float(input('Digite o valor do cateto oposto '))
ca = float(input('Digite o valor do cateto adjacente '))
hip = sqrt((co ** 2)+(ca ** 2))
print(f'O comprimento da hipotenusa é {hip}')