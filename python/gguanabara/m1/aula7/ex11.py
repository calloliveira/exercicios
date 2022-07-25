# Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta, pinta uma área de 2m²

larg = float(input('Digite a largura da parede: '))
alt = float(input('Digite a altura da parede: '))
print('Para uma área de {} m², são necessários {} lts de tinta'.format(larg*alt, (larg*alt)/2))
