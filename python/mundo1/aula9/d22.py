# Crie um programa que leia o nome completo de uma pessoa e mostre:
# >> O nome com todas as letras maiúsculas
# >> O nome com todas minúsculas
# >> Quantas letras ao todo sem considerar espaços
# >> Quantas letras tem o primeiro nome

# Resolução Carlos
'''
nome = str(input('Digite seu nome: '))
lista_nome = nome.split()
print('Seu nome em maísculo fica: {}'.format(nome.upper()))
print('Seu nome em minúsculo fica: {}'.format(nome.lower()))
print('O nome {}, contém {} caracteres'.format(nome, len(''.join(lista_nome))))
print('O primeiro contém {} letras !!!'.format(len(lista_nome[0])))

'''

# Resolução Professor

nome = str(input('Digite seu nome completo: ')).strip()
print('Seu nome em maiúsculas: {}'.format(nome.upper()))
print('Seu nome em minúsculas: {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras !!!'.format(len(nome) - nome.count(' ')))
print('Seu primeiro nome tem {}'.format(nome.find(' ')))
