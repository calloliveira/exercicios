num = int(input('Digite um número: '))
mult = 0
for c in range (2, num):
    if num % c == 0 and not num == 1 and not num == 2:
        mult = mult + 1
if mult > 0:
    print('O número {} NÃO É PRIMO, pois tem {} múltiplos no intervalo de 2 a {}!!!'.format(num, mult+2, num))
else:
    if num == 1:
        print('O número {} NÃO É considerado um NÚMERO PRIMO, pois ele faz a função de 1 e dele mesmo !!!'.format(num))
    else:
        print('O número {} É UM NÚMERO PRIMO, pois só é múltiplo de 1 e dele mesmo !!!'.format(num))