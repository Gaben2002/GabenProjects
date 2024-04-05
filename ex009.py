# Tabuada para iniciantes feita sem conceitos de repetição

# "n" vai ler o valor da tabuada
n = int(input('Valor da tabuada: '))

# print para criar uma barra superior de qualquer cor
# Se colocar uma string vezes um valor, a string irá aparecer
# quantas vezes for multiplicado ("_"*20)
# O mesmo vale para qualquer logaritimo seja adição, subtração, etc.
print('\033[31m_\033[m'*20)

'''O print pode ser utilizado em varias linhas apertando enter
antes das aspas. O {1:2}, o 1: antes dos 2 pontos determina
o numero que irá aparecer e o :2 depois dos 2 pontos determina
quantos digitos vai ter o numero que irá aparecer, se o numero
tiver um digito, o segundo digito sera um espaço em branco'''
print(f'{n} x {1:2} = {n*1}'
      f'\n{n} x {2:2} = {n*2}'
      f'\n{n} x {3:2} = {n*3}'
      f'\n{n} x {4:2} = {n*4}'
      f'\n{n} x {5:2} = {n*5}'
      f'\n{n} x {6:2} = {n*6}'
      f'\n{n} x {7:2} = {n*7}'
      f'\n{n} x {8:2} = {n*8}'
      f'\n{n} x {9:2} = {n*9}'
      f'\n{n} x {10:2} = {n*10}')

# print para criar uma barra inferior de qualquer cor
print('\033[31m_\033[m'*20)
