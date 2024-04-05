n = int(input('Numero: '))

u = n//1 % 10
d = n//10 % 10
c = n//100 % 10
m = n//1000 % 10

print(f'Unidade: \033[1;34m{u}\033[m'
      f'\nDezena: \033[1;33m{d}\033[m'
      f'\nCentena: \033[1;31m{c}\033[m'
      f'\nMilhar: \033[1;36m{m}\033[m')
