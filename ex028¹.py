from random import randint
from time import sleep

n = int(input('Numero de 0 a 5: '))

s = randint(0, 5)

print('Analisando...')
sleep(1)

if n == s:
    print(f'VOCE ACERTOU. O numero é {s}')
else:
    print(f'VOCE ERROU. O numero é {s}')
    