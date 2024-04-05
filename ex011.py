# Comprimento da parede e quantidade de tinta usada

# Lendo a altura e largura da parede
a = float(input('Altura: '))
l = float(input('Largura: '))

# Calculando o comprimento
c = l*a

# Calculando os litros de tinta usados
t = c/2

# Print formatado e com cores
print(f'Altura: \033[31m{a:.1f}\033[m'
      f'\nLargura: \033[33m{l:.1f}\033[m'
      f'\nComprimento: \033[34m{c:.1f}m²\033[m'
      f'\nTinta: \033[35m{t:.1f}l\033[m')
