#Alistamento Militar

import datetime
idade = int(input('Digite o ano que voce nasceu: '))
anos = datetime.date.today().year - idade
if anos == 18:
    print('Você já pode se alistar')
elif anos > 18:
    print('Você já passou da época de se alistar')
else:
    print('Você ainda não pode se alistar')