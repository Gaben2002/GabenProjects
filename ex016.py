# Quebrando ou arredondando um numero

# Importando somente as funções "trunc" e "floor" que quebram o numero
# Com casas decimais
from math import trunc, floor


# Somente uma variavel para o valor
n = float(input('Valor: '))


# Utilizando varios metodos de quebra de numero como por exemplo:
# n.__floor__()
# n.__trunc__()
# n.__int__() -> "Função int inclusa no python sem precisar de
# importação de qualquer módulo.
print(f'O valor: \033[1;33m{n}\033[m'
      f'\nInteiro fica: \033[1;36m{n.__floor__()}\033[m'
      f'\nE tambem: \033[1;35m{n.__int__()}\033[m'
      f'\nE tambem: \033[1;31m{n.__trunc__()}\033[m')
