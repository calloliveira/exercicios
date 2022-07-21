# Faça um programa que leia um número de 1 a 9999 e mostre na tela os dígitos separadamente
# Ex: 1834
# Unidade: 4 // Dezena: 3 // Centena: 8 // Milhar 1

#Resolução professor
nmr = int(input('Digite um número de 1 a 9999: '))
n = str(nmr)
u = nmr // 1 % 10
d = nmr // 10 % 10
c = nmr // 100 % 10
m = nmr // 1000 % 10

print('Analisa o número: {}'.format(nmr))
print('Unidade: {}'.format(u))
print('Dezena: {}'.format(d))
print('Centena: {}'.format(c))
print('Milhar: {}'.format(m))