from math import hypot

catetoOposto = float(input('informe o valor do cateto oposto: '))
catetoAdjacente = float(input('informe o valor do cateto adjacente: '))
hypotenusa = hypot(catetoOposto, catetoAdjacente)

print('O valor da hipotenusa para os catetos {} e {} e {}.'.format(catetoOposto, catetoAdjacente, hypotenusa))