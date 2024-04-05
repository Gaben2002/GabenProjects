# Trocando a ordem de uma lista

# A função "shuffle" embaralha os 4 nomes digitados
from random import shuffle

a1 = str(input('Aluno 1: '))
a2 = str(input('Aluno 2: '))
a3 = str(input('Aluno 3: '))
a4 = str(input('Aluno 4: '))

lista = [a1, a2, a3, a4]

# Depois da lista ser criada, usasse o shuffle(lista) para
# embaralhar a lista
shuffle(lista)

# Basta escrever lista no format entre as chaves que irá
# aparecer os 4 nomes embaralhados.
print(f'A ordem é'
      f'\n\033[1;36m{lista}\033[m')
