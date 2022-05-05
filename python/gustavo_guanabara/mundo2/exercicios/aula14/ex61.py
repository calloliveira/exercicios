termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))
decimo = termo + (10 - 1) * razao
c = 0
tot = 0
while c < decimo:
    if c == 0:
        c += termo
        print('{}'.format(c), end=' -> ')
    else:
        c += razao
        print('{}'.format(c), end=' -> ')
print('FIM')
