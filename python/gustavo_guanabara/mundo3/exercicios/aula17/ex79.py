valores = list()
resp = 'null'
maior = menor = 0
while True:
    valor = int(input('Digite um valor: '))
    if not valor in valores:
        valores.append(valor)
        if valor > maior or valor == 0:
            maior = valor
        if valor < menor or valor == 0:
            menor = valor
    else:
        print('Este valor já existe na lista e não será adicionado novamente!!!')
    while not resp in 'SsNn':
        resp = str(input('Deseja cadastrar novos números? [S/N] '))
    if resp in 'Nn':
        break
    else:
        resp = 'null'
print(f'Os números digitados foram: {sorted(valores)}')
print(f'Maior valor: {maior}')
print(f'Menor valor: {menor}')