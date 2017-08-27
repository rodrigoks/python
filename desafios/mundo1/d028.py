from random import randint
from time import sleep

print('==' * 40)
print('Vou pensar em um numero entre 0 e 5. Tente adivinhar...')
print('--' * 40)

escolhido = randint(0, 5)
numero = int(input('Em que numero eu pensei? '))

print('PROCESSANDO...')
sleep(3)

if numero == escolhido:
    print('Voce acertou, o numero que pensei foi {}.'.format(escolhido))
else:
    print('Voce errou, o numero que pensei foi {}.'.format(escolhido))

print('==' * 40)
