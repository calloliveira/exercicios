import moeda

p = float(input('Digite o preço: R$ '))
print(f'A metade de {p} é {moeda.metade(p)}')
print(f'O dobro de {p} é {moeda.dobro(p)}')
print(f'O valor {p} com uma correção de +10% ficaria {moeda.aumentar(p, 10)}')
print(f'O valor {p} com uma correção de -13% ficaria {moeda.diminuir(p, 13)}')