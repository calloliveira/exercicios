# Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
'''Carlos
ano = int(input('Digite o ano: '))
if ano % 400 == 0:
    print('O ano {}, é um ano bissexto !!!'.format(ano))
else:
    if ano % 4 == 0 and ano % 100 > 0:
        print ('O ano {}, é um ano bissexto !!!'.format(ano))
    else:
        print('O ano {}, não é um ano bissexto !!!'.format(ano))
'''

'''Professor - 1
ano = int(input('Que ano quer analisar? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))
'''

'''Professor - 2'''
from datetime import date
ano = int(input('Que ano quer analisar? (Coloque 0 para analisar o ano atual) '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} é BISSEXTO'.format(ano))
else:
    print('O ano {} NÃO é BISSEXTO'.format(ano))