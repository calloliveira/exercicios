# Escreva um programa que faça o computador pensar em um número inteiro de 0 a 5 e peça para
# o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá
# escrever na tela se o usuário venceu ou perdeu.

'''Carlos

import random
print('Vamos jogar?')
adv = str(input('Faça sua aposta, digite um número de 0 a 5: '))
sorteio = random.choice([0, 1, 2, 3, 4, 5])
if adv == sorteio:
    print('Parabéns, você ganhou !!!')
else:
    print('Que pena, você perdeu !!!')
print('Número sorteado: {} | Sua escolha: {}'.format(sorteio, adv))

'''

'''Professor'''
from random import randint
from time import sleep
computador = randint(0, 5)
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? '))
print('Processando...')
sleep(3)
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer! ')
else:
    print('Ganhei! Eu pensei no número {} e não no {}!'.format(computador, jogador))