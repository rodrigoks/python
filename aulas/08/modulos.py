from math import sqrt, floor
import emoji

numero = float(input('Digite um numero: '))
raiz = sqrt(numero)
print('A raiz de {} e igual a {}.'.format(numero, floor(raiz)))

print(emoji.emojize('ola mundo :earth_americas:', use_aliases=True))