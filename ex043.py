# IMC

kg = float(input('Peso: '))
m = float(input('Altura: '))

imc = kg/(m*m)

print(f'O IMC da pessoa é {imc:.2f}')

if imc < 18.5:
    print('Abaixo do peso')
if 18.5 <= imc < 25:
    print('Peso ideal')
if 25 <= imc < 30:
    print('Sobrepeso')
if 30 <= imc < 40:
    print('Obesidade')
if imc > 40:
    print('Obesidade morbida')
