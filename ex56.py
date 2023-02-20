#Analisador completo

media = 0
mmen = 0
homemvel = 0
pessoas = []
for c in range(1, 5):
    nome = str(input(f'Digite o nome da {c}ª Pessoa: '))
    idade = int(input(f'Digite a idade da {c}ª Pessoa: '))
    sexo = str(input(f'Digite o sexo da {c}ª Pessoa.\nF=Feminino.\nM=Masculino:  ')).upper()
    media = media + idade / 4
    if idade < 20 and sexo == 'F':
        mmen = mmen + 1
    if sexo == 'M':
        pessoass = [{"nome": nome, "idade": idade}]
        for c in pessoass:
            homemvel = 0
            pessoas.append(c)
            if c["idade"] > homemvel:
                homemvel = c["nome"]
print(f'A média de idade do grupo é de {media}\nO nome do homem mais velho é {homemvel}\nExistem {mmen} Mulheres abaixo dos 18 anos.')