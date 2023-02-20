#Validação de Dados
while True:
    sexo = str(input('Digite o seu sexo [M/F]: ')).upper()
    if sexo != 'F' and sexo != 'M':
        print('Opção inválida, digite novamente.')
    else:
        break
print('Sexo registrado com sucesso.')