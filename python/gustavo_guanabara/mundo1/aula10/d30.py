# Crie um programa que leia um número inteiro qualquer
# e mostre na tela se ele é par ou ímpar

'''Carlos
nmr = int(input('Digite um número para validação: '))
if nmr % 2 == 0:
    print('O número {}, é um número par !!!'.format(nmr))
else:
    print('O número {}, é um número ímpar !!!'.format(nmr))
'''

'''Professor'''
número = int(input('Me diga um número qualquer: '))
resultado = número % 2
if resultado == 0:
    print('O número {} é PAR'.format(número))
else:
    print('O número {} é ÍMPAR'.format(número))
