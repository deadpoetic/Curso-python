op = 1
n1 = 0
n2 = 0
while op == 1:
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o segundo número: '))
    op = int(input('Digite\n1=Soma.\n2=Multiplicar.\n3=Maior.\n4=Novos números.\n5=Sair.\n: '))
    while op != 1 and op != 2 and op != 3 and op != 4 and op != 5:
        print('Opção inválida, digite novamente.')
        op = int(input('Digite\n1=Soma.\n2=Multiplicar.\n3=Maior.\n4=Novos números.\n5=Sair.\n: '))
        while op == 4:
            n1 = int(input('Digite o primeiro número: '))
            n2 = int(input('Digite o segundo número: '))
            op = int(input('Digite\n1=Soma.\n2=Multiplicar.\n3=Maior.\n4=Novos números.\n5=Sair.\n: '))
    res = 0
    maior = 0
    menor = 0
    if n1 > n2:
        maior = n1
        menor = n2
    else:
        maior = n2
        menor = n1
    if n1 == n2 and op == 3:
        print('Os valores são iguais.')
    if op == 1:
        res = n1 + n2
        print(f'{n1} + {n2} é igual a {res}')
    if op == 2:
        res = n1 * n2
        print(f'{n1} * {n2} é igual a {res}')
    if op == 3 and n1 != n2:
        res = maior
        print(f'{maior} é maior que {menor}')
    if op == 5:
        print('Obrigado.')
print('Fim')