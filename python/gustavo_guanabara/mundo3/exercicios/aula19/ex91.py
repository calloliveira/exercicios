from random import randint
from time import sleep
jogadores = dict()
ranking = dict()
maior = 0
jogadores['Jogador1'] = randint(1,5)
jogadores['Jogador2'] = randint(1,5)
jogadores['Jogador3'] = randint(1,5)
jogadores['Jogador4'] = randint(1,5)
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)