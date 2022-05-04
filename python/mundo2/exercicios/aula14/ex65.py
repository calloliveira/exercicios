continua = ''
total = 0
maior = 0
menor = 0
c = 0
while continua != 'N':
    num = int(input('Digite um número: '))
    total += num
    c += 1
    if num > maior:
        maior = num
    elif num < menor or menor == 0:
        menor = num
    continua = str(input('Deseja continuar? [S/N]: ')).upper()
media = total / c
print('Você digitou {} valores, e a média entre eles é {} !'.format(c, media ))
print('Maior valor: {} | Menor valor {}'.format(maior, menor))