#Listar preços em tupla
lista_itens = ('Caneta', 2.50,
               'Pão', 7,
               'Frigideira', 59.99,
               'Caderno', 10,
               'Biscoito', 8.50)
print('=' * 36)
print('LISTAGEM DE PREÇO'.center(36))
print('=' * 36)
for item in lista_itens[0::2]:
    index_preço = lista_itens.index(item) + 1
    item_preço = f'{lista_itens[index_preço]:.02f}'
    dot = '.' * (20 - len(item))
    esp = ' ' * (8 - len(item_preço))
    print(f'{item}{dot}R${esp}{item_preço}')



#metodo alternativo
lista_itens = ('Caneta', 2.50,
               'Pão', 7,
               'Frigideira', 59.99,
               'Caderno', 10,
               'Biscoito', 8.50)
print('=' * 36)
print('LISTAGEM DE PREÇO'.center(36))
print('=' * 36)
for pos in range(0, len(lista_itens)):
    if pos % 2 == 0:
        print(f'{lista_itens[pos]:.<20}', end='')
    else:
        print(f'R${lista_itens[pos]: >7.2f}')