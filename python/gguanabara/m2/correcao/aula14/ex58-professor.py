from random import randint
computador = randint(0, 10)
print('Sou seu computador... Acabei de pensar em um número ente 0 e 10.')
print('Será que você consegue adivinhar qual foi?')
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS!!! Tente mais uma vez!')
        elif jogador > computador:
            print('MENOS!!! Tente mais uma vez!')
print('Acertou com {} tentativas!'.format(palpites))