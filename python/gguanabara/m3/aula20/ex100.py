from random import randint
from time import sleep

números = []

def sorteia(lista):
    for c in range (1, 6):
        n = randint(1,10)
        print(f'Sorteando {c}º número...[ {n} ]')
        sleep(0.2)
        lista.append(n)

def somaPar(números):
    soma = 0
    for n in números:
        if n % 2 == 0:
            soma += n
    print(f'A soma entre os pares deu {soma}...')

sorteia(números)
print('=' * 40)
print('Calculando soma dos números pares sorteados...')
print(f'Números sorteados: {números}')
sleep(1)
somaPar(números)
print('=' * 40)
