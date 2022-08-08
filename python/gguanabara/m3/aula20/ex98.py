from time import sleep
def contador(inicio, fim, passo):

    if passo == 0:
        passo = 1
    if passo < 0:
        passo = passo*-1

    cont = inicio

    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}...')

    if inicio < fim:
        while cont <= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.1)
            cont += passo        
    elif inicio > fim:
        while cont >= fim:
            print(f'{cont}', end=' ', flush=True)
            sleep(0.1)
            cont -= passo
    print('FIM')


#Program principal
contador(1, 10, 1)
contador(10, 0, 2)
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!!!')
user_start = int(input('Escolha o início: '))
user_end = int(input('Escolha o fim: '))
user_step = str(input('Escolha o passo: '))
user_step = int(user_step)
contador(user_start, user_end, user_step)
print('-=' * 20)
