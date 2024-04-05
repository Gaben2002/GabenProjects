# Primeiro e ultimo nome de uma pessoa

n = str(input('Nome Completo: ')).strip()
# Lendo o nome da pessoa com a função ".strip()" no final
# para tirar os espaços do começo e do fim

s = n.split()
# Variavel "s" para separar os nomes em uma lista e pegar a
# a posição de cada nome

print(f'Primeiro nome: \033[1;36m{s[0]}\033[m'
      # O comando {s[0]} irá mostrar o primeiro que é a posição
      # que ele se encontra (Posição 0)
      
      f'\nUltimo nome: \033[1;34m{s[len(s)-1]}\033[m')
# O comando {s[len(s)-1]} fará o programa ler o primeiro
# nome, colocando o -1 fará com que ele leia o ultimo
# independente do tamanho do nome
