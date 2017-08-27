
print('==' * 40)
print('Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.')
print('--' * 40)

seg1 = int(input('Informe o comprimento do primeiro segmento: '))
seg2 = int(input('Informe o comprimento do segundo segmento: '))
seg3 = int(input('Informe o comprimento do terceiro segmento: '))

print('PROCESSANDO...')

if seg1 < seg2 + seg3 and seg2 < seg1 + seg3 and seg3 < seg1 + seg2:
    print('Estes segmentos PODEM formar um triangulo.')
else:
    print('Estes segmentos NAO PODEM formar um triangulo.')

print('==' * 40)
