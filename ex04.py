#dissecando uma variável
n = input('Digite algo ')
print(f'Seu tipo é {type(n)}')
print(f'É número? {n.isnumeric()}')
print(f'É uma letra do alfabeto? {n.isalpha()}')
print(f'Está minúscula? {n.islower()}')
print(f'Está maiusucula? {n.isupper()}')