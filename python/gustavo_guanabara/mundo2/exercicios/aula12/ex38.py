anum = int(input('Digite um número: '))
bnum = int(input('Digite outro número: '))

if anum > bnum:
    print('O primeiro valor digitado ({}), é o maior valor !!!'.format(anum))
elif bnum > anum:
    print('O segundo valor digitado ({}), é o maior valor !!!'.format(bnum))
else:
    print('Não existe valor maior, os dois valores digitados ({} & {}), são iguais'.format(anum, bnum))