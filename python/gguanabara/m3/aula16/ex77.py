palavras = ('Teste', 'Carro', 'Busao', 'Armas', 'Fogos', 'Geladeira', 'Casa', 
            'Familia', 'Xalalau', 'Xenoubas', 'Labariebas', 'Inventor')
print('Contagem de vogais')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos: ', end='')
    for l in p:
        if l.lower() in 'aeiou':
            print(l, end=' ')