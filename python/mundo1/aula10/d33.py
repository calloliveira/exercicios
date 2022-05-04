# Faça um programa que leia 3 números e leia qual é o maior e o menor
''' Carlos
anum = int(input('Digite o 1º número: '))
bnum = int(input('Digite o 2º número: '))
cnum = int(input('Digite o 3º número: '))

if anum > bnum and anum > cnum:
    maior = anum
if bnum > cnum and bnum > anum:
    maior = bnum
if cnum > anum and cnum > bnum:
    maior = cnum
if anum < bnum and anum < cnum:
    menor = anum
if bnum < cnum and bnum < anum:
    menor = bnum
if cnum < anum and cnum < bnum:
    menor = cnum
print('Números digitados: {}, {} & {}\n Maior: {}\n Menor: {}'.format(anum, bnum, cnum, maior, menor))
'''

'''Professor'''

a = int(input('Primeiro valor: '))
b = int(input('Segundo valor: '))
c = int(input('Terceiro valor: '))

#Verificando quem é o menor
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
#Verificando quem é o menor
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print('O maior valor digitado foi {}'.format(maior))
print('O menor valor digitado foi {}'.format(menor))
