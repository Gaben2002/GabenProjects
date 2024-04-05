n = str(input('Nome: ')).strip()
# A função ".strip()" serve para tirar os espaços do inicio e
# do fim da frase e etc.

print(f'Maiusculas: \033[1;31m{n.upper()}\033[m'
      # A função "n.upper()" deixa todas as letras em maiusculas    
      
      f'\nMinusculas: \033[1;33m{n.lower()}\033[m'
      # A função "n.lower()" deixa todas as letras em minusculas
      
      f'\nLetras: \033[1;34m{len(n)-n.count(' ')}\033[m'
      # A função "len(n)" conta todas as letras digitadas 
      # incluindo espaços, para eliminar os espaços entre
      # o que foi escrito, basta digitar "-n.count(' ')
      # Essa função ira subtrair "-" os espaços contados
      # entre o que foi digitado "n.count('espaço')
      
      f'\nPrimeiro nome: \033[1;35m{n.find(' ')}\033[m')
'''Para contar as letras do primeiro nome
       Basta voce digitar "n.find('espaço')" que o programa
       irá indentificar quantas letras foram digitadas até
       ter dado o primeiro espaço, o programa procura esse
       primeiro espaço e assim que o encontra ele conta as 
       letras digitadas até sem contar o proprio espaço'''

# Forma alternativa para especificar o primeiro nome e
# contar quantas letras tem

s = n.split()
print(f'Primeiro nome: {s[0]}'
      f'\nLetras: {len(s[0])}')
'''A função "n.split()" separa as palavras digitadas e passa
para uma lista especificando cada uma com sua respectiva 
posição com um numero começando sempre do 0 
Exemplo: "Gabriel da Silva Rocha
com a função ".split() ficaria
('Gabriel', 'da', 'Silva', 'Rocha')  
     0    |   1  |  2  |   3 
Dito isso, basta digita s[0] para dizer qual o primeiro nome
e len(s[0]) para contar as letras do primeiro nome apenas.'''
