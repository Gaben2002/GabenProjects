s = float(input('Salario: '))

a = s + (s*15/100)

print(f'Salario: R$\033[1;33m{s:.2f}\033[m'
      f'\naumentou 15%'
      f'\nE virou: R$\033[1;32m{a:.2f}\033[m')
