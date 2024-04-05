a1 = float(input('Segmento 1: '))
a2 = float(input('Segmento 2: '))
a3 = float(input('Segmento 3: '))

if a1 < a2+a3 and a2 < a1+a3 and a3 < a1+a2:
    print('\033[34;1mÉ possivel fazer um triangulo\033[m')
else:
    print('\033[31;1mNão é possivel fazer um triangulo\033[m')
