a = int(input('1 valor: '))
b = int(input('2 valor: '))
c = int(input('3 valor: '))

menor = a

if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c

maior = a

if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c

print(f'O maior é \033[1;31m{maior}\033[m'
      f'\nO menor é \033[1;34m{menor}\033[m')
