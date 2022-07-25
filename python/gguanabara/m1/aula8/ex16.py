# Crie um programa que leia um número real qualquer pelo teclado e mostre na tela
# a sua porção inteira. (Mod Math)

# Resolução Carlos:
'''import math
num = float(input('Digite um número: '))
print('O número inteiro correspondente a {} é {}'.format(num, math.floor(num)))'''

# Resolução Professor
from math import trunc
num = float(input('Digite um número: '))
print('O número inteiro correspondente a {} é {}'.format(num, trunc(num)))

# Resolução Professor - 2
'''num = float(input('Digite um número: '))
print('O número inteiro correspondente a {} é {}'.format(num, int(num)))'''
