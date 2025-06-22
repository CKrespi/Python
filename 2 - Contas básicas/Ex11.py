largura = float(input('Largura da pareda: '))
altura = float(input('Altura da pareda: '))
area = largura * altura
tinta = area / 2
print('Sua parede tem a dimensão de {} x {} e sua área é de {}m2.'.format(largura, altura, area))
print('Para pintar essa parede, você precisará de {}L de tinta'. format(tinta))