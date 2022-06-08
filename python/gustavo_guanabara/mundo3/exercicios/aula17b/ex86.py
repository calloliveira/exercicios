matriz = [[], [], []]
cont = 0
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
print('=-' * 30)
print(matriz[0])
print(matriz[1])
print(matriz[2])