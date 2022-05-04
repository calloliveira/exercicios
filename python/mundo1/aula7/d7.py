# Desenvolva um programa que leia duas notas de um aluno,
# calcule e mostre a sua média

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))

print('A média entre {} & {}, é: {:.1f}'.format(n1, n2, (n1+n2)/2))