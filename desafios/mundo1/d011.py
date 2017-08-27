largura = float(input('informe a largura da parede: '))
altura = float(input('informe a altura da parede '))
area = largura * altura
quantidadeTinta = area / 2

print('A area da parede e {:.2f} e sera(ao) necessarios {:.2f} litros de tinta para pinta-la.'.format(area, quantidadeTinta))
