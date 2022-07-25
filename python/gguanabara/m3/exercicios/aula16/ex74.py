from random import randint
resp = 'null'
numeros = ()
maior = 0
menor = 0
while True:
    while not resp in 'SsNn':
        resp = str(input('Deseja gerar novos números [S/N]? '))
    if resp in 'Nn':
            break
    numeros = (randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100), randint(0, 100))  
    for num in numeros:
        print(f'{num}', end=' ')
    print(end='\n')
    print(f'Maior valor: {max(numeros)}')
    print(f'Menor valor: {min(numeros)}')
    resp = 'null'