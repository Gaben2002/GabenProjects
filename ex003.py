n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))
r = n1 + n2
print(f'\033[32m{n1}\033[m + \033[36m{n2}\033[m é igual a \033[31m{r}\033[m')

# Segunda tentativa

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))

print(f'A soma entre \033[1m{n1}\033[m e \033[4m{n2}\033[m é igual a \033[7m{n1+n2}\033[m')

# Tentativa 3

n1 = int(input('Valor 1: '))
n2 = int(input('Valor 2: '))

print(f'A subtração entre \033[45m{n1}\033[m e \033[43m{n2}\033[m é: \033[36m{n1-n2}\033[m')

# Tentativa com float

n1 = float(input('Valor 1: '))
n2 = float(input('Valor 2: '))

print(f'\033[34mA multiplicação entre\033[m'
      f'\033[32m {n1}\033[m '
      f'\033[36me\033[m '
      f'\033[36m{n2}\033[m\033[34m é igual a\033[m '
      f'\033[36m{n1*n2}\033[m')
