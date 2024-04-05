# Jogo de adivinhação

from random import randint
from time import sleep

print('\033[1;32m-=\033[m'*30)

print('\033[1;35mEstou pensando em um numero de 0 a 5, tente adivinhar qual é...\033[m')

print('\033[1;32m-=\033[m'*30)

n = int(input('Numero de 0 a 5: '))

s = randint(0, 5)

print('\033[1;33mAnalisando...\033[m')
sleep(1)

if n == s:
    print(f'\033[1;34mVOCE ACERTOU\033[m. O NUMERO É {s}.')
else:
    print(f'\033[1;31mVOCE ERROU\033[m. O NUMERO É {s}.')
