print('----- Cálculo de número fatorial -----')
num = int(input('Digite um número: '))
print('')
strnum = '{}!='.format(num)
cont = num
novonum = 0
while cont > 0:
    if cont == num:
        strnum = strnum + ' {}'.format(cont)
        cont -= 1
        novonum = num * cont
    else:
        strnum = strnum + 'x{}'.format(cont)
        cont -= 1
        if not cont == 0:
            novonum = novonum * cont
print('{} = {}'.format(strnum, novonum))
print('')
print('----- Cálculo de número fatorial -----')
