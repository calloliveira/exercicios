from random import randint
from time import sleep
jogadores = dict()
ranking = dict()
maior = 0
for c in range(0,4):
    jogadores[f'Jogador{c+1}'] = randint(1,5)
print()
print(f'{"SORTEIO":-^30}')
for k, v in jogadores.items():
    print(f'O {k} tirou {v}')
    sleep(1)
print('-' * 30)