
nome = str(input('Informe seu nome completo: '))
nomes = nome.split(' ')

print('.' * 55)
print('Seu nome em letras maiusculas {}.'.format(nome.upper()))
print('Seu nome em letras minusculas {}.'.format(nome.lower()))
print('Seu nome tem {} letras considerando espacos.'.format(len(nome)))
print('Seu nome tem {} letras desconsiderando espacos.'.format(len(nome.replace(' ', ''))))
print('O primeiro nome e {} e tem {} letras.'.format(nomes[0], len(nomes[0])))
print('.' * 55)
