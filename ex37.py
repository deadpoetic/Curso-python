#Conversor de Bases Numéricas

valor = int(input('Digite um valor: '))
opt = int(input('Digite 1 para converter em binário, 2 para octal e 3 para hexadecimal: '))
if opt == 1:
    print(bin(valor))
elif opt == 2:
    print(oct(valor))
else:
    print(hex(valor))
