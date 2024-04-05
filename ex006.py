# Dobro, Triplo e Raiz Quadrada

# Lendo o numero digitado
n = int(input('Valor: '))


# Variaveis
d = n*2
t = n*3
# r = n ** (1/2)

# É possivel utilizar a variavel "r = n ** (1/2) ou a função "pow"
# para saber a raiz quadrada do numero
print(f'\033[36mO dobro de {n} é {d:.2f}'
      f'\nO triplo de {n} é {t:.2f}'
      f'\nA raiz quadrada de {n} é {pow(n, (1/2)):.2f}\033[m')
#     f'\nA raiz quadrada de {n} é {r:.2f}
