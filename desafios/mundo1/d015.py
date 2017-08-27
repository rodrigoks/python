dias = float(input('Por quantos dias quer alugar o carro? '))
km = float(input('Quantos km pretende rodar com o carro? '))

pagoDias = dias * 60
pagoKm = km * 0.15
total = pagoDias + pagoKm

print('O valor total do aluguel sera R$ {:.2f}. R$ {:.2f} pelo aluguel e '
      'R$ {:.2f} pelos kms percorridos.'.format(total, pagoDias, pagoKm))
