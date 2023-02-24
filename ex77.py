#contando vogais em tupla
palavras = ('queijo', 'carne',
            'batata', 'toalha',
            'papel', 'biscoito')
for c in palavras:
    print(f'Na palavra {c.upper()} temos as Vogais: {c.replace("b", "").replace("c", "").replace("d", "").replace("f", "").replace("g", "").replace("h", "").replace("j", "").replace("k", "").replace("l", "").replace("m", "").replace("n", "").replace("p", "").replace("q", "").replace("r", "").replace("s", "").replace("t", "").replace("v", "").replace("x", "").replace("z", "")}')

#metodo alternativo
palavras = ('queijo', 'carne',
            'batata', 'toalha',
            'papel', 'biscoito')

for palavra in palavras:
    print(f'\nNa palavra {palavra} temos as Vogais: ', end='')
    for letra in palavra:
        if letra in 'aeiou':
           print(letra, end=' ')