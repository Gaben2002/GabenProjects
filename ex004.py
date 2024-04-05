a = input('Algo: ')

print(f'O tipo primitivo é \033[31m{type(a)}\033[m')

print(f'So tem espaços? \033[32m{a.isspace()}\033[m')

print(f'So tem numeros? \033[33m{a.isnumeric()}\033[m')

print(f'So tem letras? \033[34m{a.isalpha()}\033[m')

print(f'É alfanumerico? \033[35m{a.isalnum()}\033[m')

print(f'So tem letras maiusculas? \033[36m{a.isupper()}\033[m')

print(f'So tem minusculas? \033[36m{a.islower()}\033[m')

print(f'Esta capitalizada? \033[31m{a.istitle()}\033[m')

# "a" é considerado objeto e todo objeto tem caracteristicas
# e realiza funcionalidades (atributos e metódos)
# No exemplo acima como cada funcionalidade is tem parentes ()
# depois dele, esta sendo trabalhado os metódos
# Todo objeto string tem os metodos is "a.islower, a.isupper"


