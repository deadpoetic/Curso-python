#Aprovando Empréstimo

valor = int(input('Digite o valor da casa: '))
salario = int(input('Digite o seu salário: '))
fin = int(input('Em quantos anos você quer financiar?: '))
parcelas = fin * 12
valor1 = valor / parcelas
limite = salario * 0.3
print(limite)
print(valor1)
if valor1 < limite:
    print('Seu empréstimo foi aprovado.')
else:
    print('Seu empréstimo não foi aprovado.')