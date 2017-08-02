
frase = str(input('Digite uma frase: '))

print('A letra a aparece {} vezes na frase.'.format(frase.lower().count('a')))
print('A letra a aparece na primeira posicao no indice {}'.format(frase.lower().find('a')))
print('A letra a aparece a ultima vez no indice {}'.format(frase.lower().rfind('a')))
