# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com "Santo"

#Resolução Carlos
cidade = str(input('Digite o nome da cidade: ')).strip()
cidbroken = cidade.capitalize().split()
print('Começa com Santo? {}'.format('Santo' in cidbroken[0] ))

'''
#Resolução professor
cidade = str(input('Digite o nome da cidade: ')).strip()
print(cidade[:5].upper() == 'SANTO')
'''