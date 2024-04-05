c = str(input('Cidade: ')).strip()

print('\033[4;35mEssa cidade começa com Santo?\033[m')

print(c[:5].upper() == 'SANTO')
