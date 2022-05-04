from random import randint
from time import sleep
cont = 0
computador = randint(0, 10)
jogador = 0
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 20)
while jogador != computador:
    if cont > 0:
        print('ERROU! Tente novamente!!!')
        print('Tente novamente !!!')
    jogador = int(input('Em que número eu pensei? '))
    cont += 1
    print('Processando...')
    sleep(0.5)
print('PARABÉNS! Você conseguiu me vencer em {} tentativas!!!'.format(cont))
