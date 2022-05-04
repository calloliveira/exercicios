# Um professor quer sortear um dos seus quatro alunos para apagar o quadro.
# Faça um programa que ajude ele, lendo nome deles e escrevendo o nome do escolhido.

from random import choice
n1 = str(input('Digite o nome do 1º aluno: '))
n2 = str(input('Digite o nome do 2º aluno: '))
n3 = str(input('Digite o nome do 3º aluno: '))
n4 = str(input('Digite o nome do 4º aluno: '))
lista = [n1, n2, n3, n4]
sorteio = choice(lista)
print('O aluno escolhido foi {} !!!'.format(sorteio))