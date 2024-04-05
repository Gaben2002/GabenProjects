# Par ou ímpar

n = int(input('Numero: '))
# Lendo um numero inteiro

p = n % 2
# Todo resto da divisão vai ser 1 se o numero dividido por 2
# for impar, se for dividido por um numero par, vai ser 0

if p == 0:
    print(f'\033[34;4m{n}\033[m é par.')
else:
    print(f'\033[31;4m{n}\033[m é impar.')
# Se o numero digitado for par, o resultado da variavel p será 0
# o que irá fazer o programa mostrar a primeira condição
# "if p == 0:". se for impar irá mostrar a segunda "else:"
