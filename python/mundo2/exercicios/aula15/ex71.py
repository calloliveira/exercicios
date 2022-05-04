print('-' * 30)
print('{:^30}'.format('BANCO DO CALL'))
print('-' * 30)
valor = int(input('Quanto deseja sacar? R$ '))
print('')
totsaque = valor
cedatual = 50
totced = 0
while True:
    if totsaque >= cedatual:
        totsaque -= cedatual
        totced += 1
        if totsaque < cedatual:
            print(f'{totced} cédula(s) de {cedatual}')
    else:
        totced = 0
        if totsaque >= 20:
            cedatual = 20
        elif totsaque >= 10:
            cedatual = 10
        else:
            cedatual = 1
    if totsaque == 0:
        break
print('')