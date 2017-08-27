from time import sleep

print('==' * 40)
print('Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou ÍMPAR.')
print('--' * 40)

numero = int(input('Informe um numero? '))
paridade = numero % 2

print('PROCESSANDO...')
sleep(3)

if paridade == 0:
    print('O numero informado {} e par.'.format(numero))
else:
    print('O numero informado {} e impar.'.format(numero))

print('==' * 40)
