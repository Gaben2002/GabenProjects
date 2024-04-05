v = float(input('Velocidade atual: '))

if v <= 80:
    print('\033[1;32mDirija com segurança\033[m')
else:
    print(f'\033[1;31mMULTADO\033[m. Valor da multa \033[1;36mR${(v-80)*7:.2f}\033[m.')
