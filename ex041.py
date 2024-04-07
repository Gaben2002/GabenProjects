# Escola de Natação

from datetime import date

nasc = int(input('Ano de nascimento: '))

ano_atual = date.today().year

idade = ano_atual-nasc

print(f'O atleta tem {idade} anos')

if idade <= 9:
    print('Classificação: \033[1;34mMIRIM\033[m')
elif idade <= 14:
    print('Classificação: \033[1;36mINFANTIL\033[m')
elif idade <= 19:
    print('Classificação: \033[1;32mJUNIOR\033[m')
elif idade <= 25:
    print('Classificação: \033[1;33mSENIOR\033[m')
elif idade > 25:
    print('Classificação: \033[1;31mMASTER\033[m')

# É possivel utilizar varias condições utilizando a função "elif"
