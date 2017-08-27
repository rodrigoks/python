frase = str(input('Digite uma frase: ')).strip()

print('A letra a aparece {} vezes na frase.'.format(frase.lower().count('a')))
print('A letra a aparece na primeira posicao no indice {}'.format(frase.lower().find('a') + 1))
print('A letra a aparece a ultima vez no indice {}'.format(frase.lower().rfind('a') + 1))

