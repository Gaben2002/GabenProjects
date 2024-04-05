n = int(input('Numero inteiro: '))

print('\033[1;36m[1] BINARIO\033[m'
      '\n\033[1;35m[2] OCTAL \033[m'
      '\n\033[1;34m[3] HEXADECIMAL\033[m')
o = int(input('Escolha uma opção acima: '))

if o == 1:
    print(f'{n} convertido em \033[1;36mBINARIO\033[m é '
          f'\033[1;32m{bin(n)}\033[m')
elif o == 2:
    print(f'{n} convertido em \033[1;35mOCTAL\033[m é '
          f'\033[1;32m{oct(n)}\033[m')
elif o == 3:
    print(f'{n} convertido em \033[1;34mHEXADECIMAL\033[m é '
          f'\033[1;32m{hex(n)}\033[m')
else:
    print('\033[31;1mOPÇÃO INVALIDA\033[m')
