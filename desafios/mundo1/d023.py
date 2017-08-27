
numero = str(input('Informe um numero de 0-9999: '))

if len(numero) < 4:
    numero = numero.zfill(4)

print('unidade {}.'.format(numero[3]))
print('dezena {}.'.format(numero[2]))
print('centena {}.'.format(numero[1]))
print('milhar {}.'.format(numero[0]))
