s = float(input('Salario: '))

if s <= 1250:
    print(f'De \033[1;31m{s}\033[m '
          f'irá ganhar \033[34;1m{s+(s*15/100)}\033[m')
else:
    print(f'De \033[1;31m{s}\033[m '
          f'irá ganhar \033[34;1m{s+(s*10/100)}\033[m')
