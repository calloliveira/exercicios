from random import randint
from time import sleep

números = []

def sorteia():
    for c in range (1, 6):
        print(f'Sorteando {c}º número...')
        sleep(1)
        números.append(randint(1,100))

def somaPar(números):
    soma = 0
    for n in números:
        if n % 2 == 0:
            soma += n
    print(f'A soma entre os pares deu {soma}')

sorteia()
print('Calculando soma dos números pares sorteados...')
print(f'Números sorteados: {números}')
sleep(2)
somaPar(números)
