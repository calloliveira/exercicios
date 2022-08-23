from time import sleep

def maior(* valores):
    maior = 0
    print('=' * 20)
    print('Analisando os valores...')
    for n in valores:
        print(n, end=' ', flush=True)
        sleep(0.1)
        if n > maior:
            maior = n
    print(f'\nForam digitados {len(valores)} valores...')
    print(f'O maior valor digitado foi {maior}')

maior(4, 5, 7)
maior(5, 7, 9, 3, 2, 6)
maior(100, -80, 99, 117, 98, 1010)
print('=' * 20)
