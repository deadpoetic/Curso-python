#Analisador de Textos
nome = str(input('Digite o seu nome: '))
maiu = nome.upper()
minu = nome.lower()
letras = nome.strip()
lista = nome.split()
juntar = ''.join(lista)
letrastodo = len(juntar)
letrasprim = lista[0]
print(f"""Nome com letras maiusculas {maiu}
      nome com letras minusculas {minu}
      Quantas letras ao todo {len(juntar)}
      Quantas letras tem o primeiro nome {len(letrasprim)}""")
