# Crie um programa que leia uma frase no teclado e mostre:
# Quantas vezes aparece a letra 'A'
# Em que posição ela aparece a primeira vez
# Em que posição ela aparece pela última vez

'''
#Resolução Carlos - incompleto
frase = str(input('Digite uma frase: '))
print('Temos {} ocorrência(s) da letra A !!!'.format(frase.lower().count('a')))
print('A letra A aparece pela primeira vez no carácter de nmr {}'.format(frase.find('a')))
'''

#Resolução professor
frase = str(input('Digite uma frase: ')).strip().lower()
print('Temos {} ocorrência(s) da letra A !!!'.format(frase.count('a')))
print('A letra A aparece pela primeira vez no carácter de nmr {}'.format(frase.find('a')+1))
print('A letra A apare pela última vez no carácter de nmr {}'.format(frase.rfind('a')+1))