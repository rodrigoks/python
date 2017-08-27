from math import cos, sin, tan, radians

angulo = float(input('informe o valor de um angulo: '))

cosseno = cos(radians(angulo))
seno = sin(radians(angulo))
tangente = tan(radians(angulo))

print('O seno do angulo {} e {:.2f}.'.format(angulo, seno))
print('O cosseno do angulo {} e {:.2f}.'.format(angulo, cosseno))
print('O tangente do angulo {} e {:.2f}'.format(angulo, tangente))
