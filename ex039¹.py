# Serviço Militar 

from runpy import run_path
from datetime import date
# Importando "run_path" do módulo "runpy" para reiniciar o programa caso o sexo digitado seja inválido
# Importando "date" do módulo "datetime" para ver o ano atual

nasc = int(input('Ano de nascimento: '))
# Lendo o ano de nascimento da pessoa

print('Escolha o sexo:'
      '\n[1] Feminimo'
      '\n[2] Masculino')
sexo = int(input('Sexo: '))
# Especificando o sexo da pessoa para saber se é necessario prestar serviço militar ou não

ano_atual = date.today().year
# A função "date.today().year" mostra o ano atual

idade = ano_atual-nasc
# Para mostar a idade da pessoa, basta subtrair o ano atual com o ano de nascimento da pessoa "ano_atual - nasc"

if sexo == 1:
    print('Mulheres não são obrigadas a prestar serviço Militar no Brasil')
    quit()
# A função "quit()" finaliza o programa caso a pessoa seja mulher

if sexo == 3:
    print('Digite um numero válido')
    run_path("ex039.py")
# A função "run_path("ex039.py") reinicia o programa especificando o nome do programa entre parenteses

if sexo == 2:
    print(f'O homem que nasceu em {nasc} tem {idade} anos em {ano_atual}')
if idade < 18:
    print(f'Faltam \033[1;34m{18-idade}\033[m anos para voce se alistar'
          f'\nSeu ano de alistamento é em \033[1;34m{nasc+18}\033[m')
elif idade > 18:
    print(f'Voce deveria ter se alistado há \033[1;31m{idade-18}\033[m anos'
          f'\nSeu ano de alistamento foi em \033[1;31m{nasc+18}\033[m')
elif idade == 18:
    print(f'Voce deve se alistar \033[1;36mIMEDIATAMENTE\033[m')
quit()
# A função quit() aqui no final serve para não duplicar o prints sobre a idade e ano de alistamento da pessoa


