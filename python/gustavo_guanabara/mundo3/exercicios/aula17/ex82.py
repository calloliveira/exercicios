valores = list()
ivalores = list()
pvalores = list()
resp = 'null'
while True:
    valores.append(int(input('Digite um valor: ')))
    while not resp in 'SsNn':
        resp = str(input('Deseja continuar? [S/N] '))
    if resp in 'Nn':
        break
    resp = 'null'
print(valores)
for v in valores:
    if v % 2 == 0:
        pvalores.append(v)
    else:
        ivalores.append(v)
print(f'Valores digitados: {valores}')
print(f'Valores ímpares: {sorted(ivalores)}')
print(f'Valores pares: {sorted(pvalores)}')
