print('=' * 30)
print('Análise de strings')
print('=' * 30)
pares = ''
valor1 = int(input('Digite um valor: '))
valor2 = int(input('Digite outro valor: '))
valor3 = int(input('Digite outro valor: '))
valor4 = int(input('Digite outro valor: '))
valortup = (valor1, valor2, valor3, valor4)
for cont in valortup:
    if cont % 2 == 0:
        pares += (' ' + str(cont))
print('=' * 30)
print('Resultado')
print('=' * 30)
print(f'Ocorrências do nº 9: {valortup.count(9)}')
print(f'Primeira ocorrência do nº 3: {valortup.index(3)+1}')
print(f'Números pares: {pares}')
print('=' * 30)