# O mesmo professor do desafio anterior quer sortear a ordem de apresentação de trabalho dos alunos.
# Faça um programa que leia o nome dos quatro aluno e mostre a ordem sorteada.
from random import shuffle
n1 = str(input('Nome 1º aluno: '))
n2 = str(input('Nome 2º aluno: '))
n3 = str(input('Nome 3º aluno: '))
n4 = str(input('Nome 4º aluno: '))
lista = [n1, n2, n3, n4]
shuffle(lista)
print('A ordem de apresentação será: {}'.format(lista))