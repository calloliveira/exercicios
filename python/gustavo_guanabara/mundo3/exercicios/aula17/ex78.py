valores = list()
maior = menor = 0
for c in range (0, 5):
    valores.append(int(input('Digite um valor: ')))
for v in valores:
    if v > maior or maior == 0:
        maior = v
    if v < menor or menor == 0:
        menor = v
print(f'O maior valor digitado foi {maior} e sua posição na lista é a {valores.index(maior)}ª')
print(f'O menor valor digitado foi {menor} e sua posição na lista é a {valores.index(menor)}ª')

