v = float(input('Valor da casa: '))
s = float(input('Salario: '))
a = int(input('Anos: '))

p = v / (a*12)

m = s*30/100

print(f'Pagando uma casa de R${v} em {a} anos, fica R${p:.2f}')

if p <= m:
    print('\033[34;1mEmpréstimo CONCEDIDO.\033[m')
else:
    print('\033[31;1mEmpréstimo NEGADO\033[m')
