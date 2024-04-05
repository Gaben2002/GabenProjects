# Conversor de real para dólar

# Lendo o numero em real
r = float(input('Valor em real R$'))

# Variavel conversor para dolar
d = r/4.98

# Print com cores e formatado
print(f'\033[4;32mR${r:.2f}\033[m'
      f'\nEm dólar é'
      f'\n\033[4;36mUS${d:.2f}\033[m')

# Conversor de real para euro

# Lendo o numero em real
r = float(input('Valor em real R$'))

# Variavel conversor para euro
e = r/5.38

# Print com cores e formatado
print(f'\033[4;31mR${r:.2f}\033[m'
      f'\nEm euro é'
      f'\n\033[4;33mEU${e:.2f}\033[m')
