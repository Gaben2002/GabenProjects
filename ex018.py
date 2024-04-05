from math import sin, cos, tan, radians

a = float(input('Angulo: '))
s = sin(radians(a))
c = cos(radians(a))
t = tan(radians(a))

print(f'Angulo: \033[31m{a:.2f}\033[m'
      f'\nSeno: \033[33m{s:.2f}\033[m'
      f'\nCosseno: \033[34m{c:.2f}\033[m'
      f'\nTangente: \033[36m{t:.2f}\033[m')
