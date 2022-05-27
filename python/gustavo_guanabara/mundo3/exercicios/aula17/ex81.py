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
print('-=' * 30)
print(f'A lista contém {len(valores)} valores!!!')
#print(f'Lisa em forma decrescente: {valores[::-1]}')
valores.sort(reverse=True)
print(f'Lisa em forma decrescente: {valores}')
if 5 in valores:
    print(f'Valor 5 encontrado na posição {valores.index(5)}')
else:
    print('O valor 5 não foi encontrado na lista')
print('-=' * 30)
