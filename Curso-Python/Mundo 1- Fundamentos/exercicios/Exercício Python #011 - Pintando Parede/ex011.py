larg = float(input('digite a largura da parede:'))
alt = float(input('digita a altura da parede: '))
area = alt * larg
tinta = area/2
print('a parede tem a dimensão de {}x{} e sua area é de {}m²,'.format(larg, alt, area))
print(' para pinta-la serão necessários {} litros de tinta'.format(tinta))
