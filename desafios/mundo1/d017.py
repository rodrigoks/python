from math import hypot

catetoOposto = float(input('informe o valor do cateto oposto: '))
catetoAdjacente = float(input('informe o valor do cateto adjacente: '))
hypotenusa = hypot(catetoOposto, catetoAdjacente)

print('O valor da hipotenusa para os catetos {:.2f} e {:.2f} e {:.2f}.'
      .format(catetoOposto, catetoAdjacente, hypotenusa))
