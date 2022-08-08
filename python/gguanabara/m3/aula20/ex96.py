def area(l, c):
    total = l * c
    print(f'A área do total de um terreno de {l} x {c} é de {total} M²...')

#Program Principal
print('-' * 20)
print('Cálculo de terrenos')
print('-' * 20)
largura = float(input('Digite a largura: '))
comprimento = float(input('Digite o comprimento: '))
area(largura, comprimento)