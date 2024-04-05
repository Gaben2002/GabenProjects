# Procurando as posições de uma letra especificada

f = str(input('Frase: ')).strip()
# Lendo uma frase qualquer com a função ".strip" no final
# para tirar os espaços do começo e fim

print(f'Letras M: \033[1;34m{f.lower().count('m')}\033[m'
      '''Para contar as letras especificada em uma frase
       é necessario o uso do f.lower() para deixar todas
       as letras em minusculas, logo em seguida se usa 
       ".count('m')", a letras entre aspas e parenteses
       nessa função tem que estar em minuscula para assim
       o programa funcionar corretamente e sempre identificar
       a letra "m" mesmo escrito em maiusculas ou minuscula
       É possivel fazer ao contrario utilizando a função 
       f.upper().count('M'), o ".upper" deixa todas as letras
       em maiusculo, logo o M entre aspas e parenteses na
       função .count() tem que ser em maiusculo'''
      
      f'\nPrimeiro M: \033[1;33m{f.lower().find('m')+1}\033[m'
      '''Para descobrir a posição da primeira letra especificada
      basta utilizar f.lower().find('m') ou f.upper().find('M').
      O python começa a contagem do 0, porem nos sempre começamos
      do 1, por isso basta digitar "+1" no final da função
      para ver a posição que nós vemos'''
      
      f'\nUltimo M: \033[1;31m{f.lower().rfind('m')+1}\033[m')
'''Para descobri a posição da ultima letra especificada
basta fazer quase do mesmo jeito de antes, a unica diferença
é que iremos usar a função "rfind('m'), isso fara com que o
programa comece a procurar a letra começando pela direita'''