print('==' * 40)
print('Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.')
print('--' * 40)

distancia = int(input('Qual a distancia da viagem? '))
valorProximo = 0.5
valorLonge = .45

print('PROCESSANDO...')

if distancia > 200:
    preco = distancia * valorLonge
else:
    preco = distancia * valorProximo

print('O custo da viagem sera de R$ {:.2f}.'.format(preco))

print('==' * 40)
