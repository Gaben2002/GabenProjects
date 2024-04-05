from datetime import date

a = int(input('Ano, 0 para o ano atual: '))

if a == 0:
    a = date.today().year

if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print(f'\033[1;32m{a}\033[m é bissexto')
else:
    print(f'\033[1;31m{a}\033[m não é bissexto')

# O sinal de "!=" significa que tal coisa tem que ser diferente
# de outra coisa