l = float(input('Qual é a largura da parede em metros? '))
a = float(input('Qual é a altura da parede em metros? '))
area = l * a
litros = (l*a)/2
print('A área da parede é de {:.2f} metros² e são necessários {:.2f} litros de tinta para pintá-la'
      .format(area,litros))
