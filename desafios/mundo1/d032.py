from datetime import date

print('==' * 40)
print('Faça um programa que leia um ano qualquer e mostre se ele é bissexto.')
print('--' * 40)

ano = int(input('Informe um ano com 4 digitos? Coloque 0 para o ano atual: '))

if ano == 0:
    ano = date.today().year

print('PROCESSANDO...')

if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano informado({}) e bissexto'.format(ano))
else:
    print('O ano informado({}) nao e bissexto'.format(ano))

print('==' * 40)

