from random import randint, choice
itens = ['Pedra', 'Papel', 'Tesoura']
print(''' OPÇÕES

[0] - Pedra
[1] - Papel
[2] - Tesoura

''')
computador = choice(itens)
jogador = int(input('Qual a sua escolha? '))


