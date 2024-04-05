d = float(input('Distancia: '))

if d <= 200:
    print(f'O preço é {d*0.5:.2f}')
else:
    print(f'O preço é {d*0.45:.2f}')
