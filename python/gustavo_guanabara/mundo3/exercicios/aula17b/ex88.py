from random import randint
from time import sleep
jogo = list()
jogos = list()
print('=-' * 30)
print('SIMULADOR DE APOSTAS MEGA SENA')
print('=-' * 30)
njogos = int(input('Quantidade de apostas: '))
for c in range(0,njogos):
    for n in range(0,6):
        while len(jogo) < 6:
            sorteio = randint(1,60)
            if not sorteio in jogo:
                jogo.append(sorteio)
    jogos.append(jogo[:])
    jogo.clear()
print('=-' * 30)    
for i, j in enumerate(jogos):
    print(f'{i+1}º Jogo: {sorted(j)}')
    sleep(0.5)
print(f'{">BOA SORTE<":=^30}')
print('=-' * 30)