from random import randint
from time import sleep
from operator import itemgetter
jogadores = dict()
ranking = list()
sorteio = c = 0
while len(jogadores) != 4:
    sorteio = randint(1,6)
    if not sorteio in jogadores.values():
        c += 1
        jogadores[f'Jogador{c}'] = sorteio
print()
print(f'{"SORTEIO":-^30}')
for k, v in jogadores.items():
    print(f'O {k} tirou {v} no dado...')
    sleep(1)
print('-' * 30)
print(f'{"RANKING":-^30}')
ranking = sorted(jogadores.items(), key=itemgetter(1), reverse=True)
for i, v in enumerate(ranking):
    print(f'{i+1}º: {v[0]} com {v[1]} pontos...')
    sleep(1)
print('-' * 30)
