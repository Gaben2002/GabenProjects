# Calculando descontos

# Lendo o preço do produto
p = float(input('Preço: R$'))

d = p - (p*5/100)

print(f'De \033[4;31mR${p:.2f}\033[m'
      f'\nCom 5% de desconto é'
      f'\n\033[4;32mR${d:.2f}\033[m')
