from time import sleep
def contador(inicio, fim, passo):
    cont = 0
    print('-=' * 20)
    if passo == 0:
        passo = 1
    if passo < 0:
        passo = passo*-1
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}...')
    cont = inicio
    if inicio < fim:
        while cont <= fim:
            print(f'{cont}', end=' ')
            cont += passo
    elif inicio > fim:
        while cont >= fim:
            print(f'{cont}', end=' ')
            cont -= passo
    print('FIM')
    print('-=' * 20)
contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez de personalizar a contagem!!!')
user_start = int(input('Escolha o início: '))
user_end = int(input('Escolha o fim: '))
user_step = str(input('Escolha o passo: '))
if user_step == '':
    user_step = '1'
user_step = int(user_step)
contador(user_start, user_end, user_step)

