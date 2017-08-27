
nome = str(input('Informe seu nome completo: '))
nomes = nome.split(' ')

print('Seu nome em letras maiusculas {}.'.format(nome.upper()))
print('Seu nome em letras minusculas {}.'.format(nome.lower()))
print('Seu nome tem {} letras considerando espacos.'.format(len(nome)))
print('Seu nome tem {} letras desconsiderando espacos.'.format(len(nome.replace(' ', ''))))
print('O primeiro nome e {}.'.format(nomes[0]))