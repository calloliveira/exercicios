palavras = ('Teste', 'Carro', 'Busao', 'Armas', 'Fogos', 'Geladeira', 'Casa', 'Familia', 'Computador', 'Vegetal', 'Televisao', 'Inventor')
print('Contagem de vogais')
for cont in palavras:
    cont = cont.lower()
    print(f'{cont.upper()} - A: {cont.count("a")} / E: {cont.count("e")} / I: {cont.count("i")} / O: {cont.count("o")} / U: {cont.count("u")} ')
    