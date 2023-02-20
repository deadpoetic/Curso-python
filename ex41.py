#Classificando Atletas

import datetime
nasc = int(input('Digite o ano que você nasceu: '))
ano = datetime.date.today().year - nasc
if ano <= 9:
    print('Você está na categoria mirim.')
elif ano <= 14:
     print('Você está na categoria infantil')
elif ano <= 19:
     print('Você está na categoria junior')
elif ano == 20:
     print('Você está na categoria sênior')
else:
    print('Você está na categoria master')