#Gerenciador de Pagamentos

valor = float(input('Digite o valor do produto: '))
metodo = int(input('Digite\n1-À vista no dinheiro.\n2-À vista no cartão.\n3-Em até 2x.\n4-3x ou mais.\nDigite aqui a opção:'))
final = 0
if metodo == 1:
    print(f'Valor a final a se pagar com 10% de desconto {valor * 0.9}')
elif metodo == 2:
    print(f'Valor final a se pagar com 5% de desconto {valor * 0.95}')
elif metodo == 3:
    print(f'Valor final a se pagar sem desconto {valor}')
else:
    print(f'Valor final a se pagar com 20% de juros {valor * 1.2}')