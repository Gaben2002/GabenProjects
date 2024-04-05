# Catetos e hipotenusas

# Importando somente o "hypot" do módulo "math"
from math import hypot

# Variaveis do cateto e hipotenusa utilizando "hypot"
co = float(input('Cateto oposto: '))
ca = float(input('Cateto adjacente: '))
hi = hypot(co, ca)

# Utilizando calculo matematico para calcular hipotenusa
# hi = (co ** 2 + ca ** 2) ** (1/2)

print(f'Hipotenusa: \033[31m{hi:.2f}\033[m')
