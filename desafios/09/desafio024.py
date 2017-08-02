
numero = str(input('Informe um numero de 0-9999: '))

if len(numero) < 4:
    numero = numero.zfill(4)

print('unidade {}.'.format(numero[len(numero)-1: len(numero)]))
print('dezena {}.'.format(numero[len(numero)-2: len(numero)-1]))
print('centena {}.'.format(numero[1: 2]))
print('milhar {}.'.format(numero[0: 1]))