valores = [[], [], []]
for cont in range(0,7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        valores[0].append(valor)
    else:
        valores[1].append(valor)    
for v1 in valores[0]:
    valores[2].append(v1)
for v2 in valores[1]:
    valores[2].append(v2)
print('=-' * 30)
print('Valores Organizados')
print('=-' * 30)
print(f'Lista ordenada: {sorted(valores[2])}')
print(f'Valores pares: {sorted(valores[0])}')
print(f'Valores ímpares: {sorted(valores[1])}')
print(f'Lista completa: {valores}')