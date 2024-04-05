dias = int(input('Dias: '))
km = float(input('Km: '))

pago = (dias*60)+(km*0.15)

print(f'O total é: R$\033[1;33m{pago:.2f}\033[m')
