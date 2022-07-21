# Faça um programa que leia o nome completo de uma pessoa e mostre separadamente
# o primeiro e ultimo nome

#Resolução Carlos
nome = str(input('Digite seu nome completo: ')).strip()
lista_nome = nome.split()
print('O primeiro nome é {}'.format(lista_nome[0]))
print('O último nome é {}'.format(lista_nome[len(lista_nome)-1]))