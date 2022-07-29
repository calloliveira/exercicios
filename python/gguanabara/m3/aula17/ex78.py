valores = list()
maior = menor = 0
for c in range (0, 5):
    valores.append(int(input('Digite um valor: ')))
    if valores[c] > maior or maior == 0:
        maior = valores[c]
    if valores[c] < menor or menor == 0:
        menor = valores[c]
print(f'O maior valor digitado foi {maior} nas posições ', end='')
for i, v in enumerate(valores):
    if v == maior:
        print(f'{i}... ',end='')
print()
print(f'O menor valor digitado foi {menor} nas posições ', end='')
for i, v in enumerate(valores):
    if v == menor:
        print(f'{i}...', end='')
print()

