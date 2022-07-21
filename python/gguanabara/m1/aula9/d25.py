# Crie um programa que leia o nome completo de uma pessoa e diga se ela tem "Silva" no nome

#Resolução Carlos
nome = str(input('Digite o seu nome completo: ')).strip()
print('O nome contém Silva? {}'.format('Silva' in nome.title()))