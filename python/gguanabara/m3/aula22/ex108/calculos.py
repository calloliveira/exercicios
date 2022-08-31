import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print(f'O valor {moeda.moeda(p)} com uma correção de +10% ficaria {moeda.moeda(moeda.aumentar(p, 10))}')
print(f'O valor {moeda.moeda(p)} com uma correção de -13% ficaria {moeda.moeda(moeda.diminuir(p, 13))}')