n = str(input('Nome: ')).strip()

print(f'Maiusculas: {n.upper()}'
      f'\nMinusculas: {n.lower()}'
      f'\nLetras: {len(n)-n.count(' ')}'
      f'\nPrimeiro: {n.find(' ')}')
