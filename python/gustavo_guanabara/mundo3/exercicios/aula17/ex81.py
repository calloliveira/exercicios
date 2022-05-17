valores = list()
resp = 'null'
while True:
    valores.append(int(input('Digite um valor: '))) 
    while not resp in 'SsNn':
        resp = str(input('Deseja cadastrar novos números? [S/N] '))
    if resp in 'Nn':
        break
    else:
        resp = 'null'
print(f'A lista contém {len(valores)} valores!!!')
print(f'Elementos da lista: {valores[]}')
