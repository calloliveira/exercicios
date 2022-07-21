valores = list()
for cont in range (0,5):
    valor = int(input('Digite um valor: '))
    if valores == [] or valor > valores[-1]:
        valores.append(valor)
        print('Adicionado ao final da lista')
    else:
        pos = 0
        while pos < len(valores):
            if valor < valores[pos]:
                valores.insert(pos, valor)
                print(f'Adicionado na posição {pos} da lista')
                break
            pos += 1
print('-=' * 30)
print(f'Os valores digitados foram: {valores}')