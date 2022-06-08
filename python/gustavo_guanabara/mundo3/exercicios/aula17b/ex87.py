matriz = [[], [], []]
cont = 0
vpares = vcol3 = vm2l = 0
print('=-' * 30)
print('Criador de matrizes')
print('=-' * 30)
for c in range(0,3):
    cont += 1
    matriz[0].append(int(input(f'Digite o {cont}º valor da linha 0 da matriz: ')))
cont = 0
for c in range(0,3):
    cont += 1
    matriz[1].append(int(input(f'Digite o {cont}º valor da linha 1 da matriz: ')))
cont = 0
for c in range(0,3):
    cont += 1
    matriz[2].append(int(input(f'Digite o {cont}º valor da linha 2 da matriz: ')))
for v1 in matriz[0]:
    if v1 % 2 == 0:
        vpares += v1
for v2 in matriz[1]:
    if v2 > vm2l:
        vm2l = v2
    if v2 % 2 == 0:
        vpares += v2
for v3 in matriz[2]:
    vcol3 += v3
    if v3 % 2 == 0:
        vpares += v3
print('=-' * 30)
print('Criador de matrizes')
print('=-' * 30)
print(matriz[0])
print(matriz[1])
print(matriz[2])
print('=-' * 20)
print('Tratamento dos números')
print('=-' * 20)
print(f'Soma dos valores pares: {vpares}')
print(f'Soma 3ª coluna: {vcol3}')
print(f'Maior valor 2ª coluna: {vm2l}')