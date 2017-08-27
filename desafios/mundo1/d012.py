valor = float(input('informe o preco do produto para saber o valor com desconto: '))
valor = valor - (valor * 5 / 100)

print('Com o desconto o novo valor e {:.2f}'.format(valor))
