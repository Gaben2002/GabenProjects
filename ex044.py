# Formas de pagamento

# Para calcular o Juros em porcentagem, basta colocar "preço+(preço*porcentagem desejada/100)".

# Para calcular desconto é a mesma coisa, mas invés de somar voce subtrai "preço-()".

from runpy import run_path

preço = float(input('Preço: R$'))

print('FORMAS DE PAGAMENTO'
      '\n[1] à vista \033[32;1mdinheiro/cheque\033[m'
      '\n[2] à vista \033[34;1mcartão\033[m'
      '\n[3] \033[33;1m2x no cartão\033[m'
      '\n[4] \033[31;1m3x ou mais no cartão\033[m')
opcao = int(input('Escolha: '))

if opcao > 4:
    print('\033[31;1mOpção Invalida\033[m, Digite uma opção válida')
    run_path('ex044.py')
if opcao == 1:
    desconto = preço - (preço*10/100)
    print(f'Compra de \033[34;1mR${preço:.2f}\033[m, '
          f'\033[32;1m10%\033[m de desconto \033[36;1mR${desconto:.2f}\033[m')
elif opcao == 2:
    desconto = preço - (preço*5/100)
    print(f'Compra de \033[34;1mR${preço:.2f}\033[m, '
          f'\033[32;1m5%\033[m de desconto \033[36;1mR${desconto:.2f}\033[m')
elif opcao == 3:
    duas = preço/2
    print(f'Compra de \033[34;1mR${preço:.2f}\033[m, '
          f'\033[33;1m2x\033[m no cartão \033[35;1mR${duas:.2f}\033[m')
elif opcao == 4:
    quant = int(input('Parcelas: '))
    if quant < 3:
        parc = preço / quant
        print(f'\033[32;1m{quant}x\033[m fica \033[36;1mR${parc:.2f}\033[m')
        quit()
    juros = preço + (preço*20/100)
    mais = juros/quant
    print(f'Compra parcelada em \033[32;1m{quant}x\033[m de \033[34;1mR${mais:.2f}\033[m'
          f'\n\033[34;1mR${preço}\033[m JUROS de \033[31;1mR${juros:.2f}\033[m')
quit()
