palavras = ('Teste', 'Carro', 'Busao', 'Armas', 'Fogos', 'Geladeira', 'Casa', 
            'Familia', 'Computador', 'Vegetal', 'Televisao', 'Inventor')
print('Contagem de vogais')
for p in palavras:
    print(f'\nA palavra {p.upper()} tem as vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra.lower(), end=' ')