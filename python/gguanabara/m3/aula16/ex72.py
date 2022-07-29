palavras = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco', 'Seis', 'Sete', 'Oito', 
            'Nove', 'Dez', 'Onze', 'Doze', 'Treze', 'Quatorze', 'Quinze', 
            'Dezesseis', 'Dezessete', 'Dezoito', 'Dezenove', 'Vinte')
resp = 'null'
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if not num < 0 and not num > 20:
        print(f'Você digitou o número {palavras[num]}')
        if not resp in 'SsNn':
            resp = str(input('Deseja continuar? [S/N] '))
            if resp in 'Nn':
                break
        resp = 'null'
            