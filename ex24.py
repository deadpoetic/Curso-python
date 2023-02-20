#Verificando as primeiras letras de um texto

cidade = str(input('Digite o nome da sua cidade: ')).upper()
lista = cidade.split()
checar = lista[0]
teste = 'SANTO' in checar
print(teste)
