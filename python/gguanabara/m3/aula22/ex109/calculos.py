import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {moeda.moeda(p)} é {moeda.metade(p, True)}')
print(f'O dobro de {moeda.moeda(p)} é {moeda.dobro(p, True)}')
print(f'O valor {moeda.moeda(p)} com uma correção de +10% ficaria {moeda.aumentar(p, 10, True)}')
print(f'O valor {moeda.moeda(p)} com uma correção de -13% ficaria {moeda.diminuir(p, 13, True)}')