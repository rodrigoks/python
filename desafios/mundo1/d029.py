from time import sleep

print('==' * 40)
print('Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.')
print('--' * 40)

velocidade = int(input('Qual a velocidade do carro? '))
limite = 80
multaPorkmHora = 7

print('PROCESSANDO...')
sleep(3)

if velocidade > limite:
    print('Voce ultrapassou o limite de velocidade {} km/h.'.format(limite))
    print('Sera multado em R$ {:.2f}.'.format((velocidade - limite) * multaPorkmHora))
else:
    print('Voce esta andando dentro do limite de {} km/h.'.format(limite))

print('==' * 40)
