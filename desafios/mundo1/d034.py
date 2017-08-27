
print('==' * 40)
print('Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.')
print('--' * 40)

salario = int(input('Informe o valor do seu salario (R$): '))
limite = 1250

print('PROCESSANDO...')

if salario > limite:
    novoSalario = salario * 1.1
else:
    novoSalario = salario * 1.15

print('O valor do novo salario apos o aumento sera de R$ {}.'.format(novoSalario))

print('==' * 40)
