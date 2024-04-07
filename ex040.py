n1 = float(input('Nota 1: '))
n2 = float(input('Nota 2: '))

media = (n1+n2)/2

print(f'{n1} e {n2}, a média é {media:.1f}')

if media >= 7:
    print('Aprovado')
elif 7 > media >= 5:
    print('Recuperação')
elif media < 5:
    print('Reprovado')
