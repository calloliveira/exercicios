matriz = [[], [], []]
cont = 0
print('=-' * 30)
print('Criador de matrizes')
print('=-' * 30)
for c in range(0,3):
    cont += 1
    matriz[0].append(int(input(f'Digite o elemento (0, {c}): ')))
cont = 0
for c in range(0,3):
    cont += 1
    matriz[1].append(int(input(f'Digite o elemento (1, {c}): ')))
cont = 0
for c in range(0,3):
    cont += 1
    matriz[2].append(int(input(f'Digite o elemento (2, {c}): ')))
print('=-' * 30)
print('Criador de matrizes')
print('=-' * 30)
for c in matriz[0]:
    print(f'[ {c} ]', end=' ')
print(end='\n')
for c in matriz[1]:
    print(f'[ {c} ]', end=' ')
print(end='\n')
for c in matriz[2]:
    print(f'[ {c} ]', end=' ')