n = int(input('\033[31mDigite um numero: \033[m'))
a = n - 1
s = n + 1
print(f'\033[36mAnalisando o valor\033[m '
      f'\033[32m{n}\033[m, \033[34mseu antecessor é\033[m '
      f'\033[33m{a}\033[m '
      f'e seu sucessor é \033[35m{s}\033[m')

# Tentativa 2

n = int(input('Valor: '))

a = n - 1

s = n+1

print(f'O antecessor de {n} é {a}, sucessor é {s}')

# tentativa 3

n = int(input('Valor: '))

a = n - 1
s = n + 1

print(f'O antecessor de {n} é {a}, o sucessor {s}')
