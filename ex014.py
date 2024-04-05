c = float(input('Temperatura em C°: '))

f = (c*9/5)+32

print(f'De \033[31m{c:.1f}C°\033[m'
      f'\nficou \033[34m{f:.1f}F°\033[m.')
