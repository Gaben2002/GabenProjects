preço = float(input('Qual é o preço do produto? R$'))
aumento = preço + (preço * 3 / 100)
desconto = preço - (preço * 10 / 100)
print('Caso o cliente pague a vista ele tera um desconto de 10% e o produto sairá pro R${}'.format(desconto))
print('caso o produto seja parcelado, haverá um aumento de 3%, cujo o aumento inicial sairá por R${}'.format(aumento))
