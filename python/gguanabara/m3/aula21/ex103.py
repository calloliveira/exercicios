def ficha(nome='<Desconhecido>', gols='0'):
    print(f'O jogador {nome} fez {gols} gol(s) no campeonato...')


#Programa Principal
n = str(input('Nome do jogador: '))
g = str(input('Número de gols: '))

if n and g.isnumeric():
    ficha(n, g)
elif n and not g.isnumeric():
    ficha(nome=n)
elif not n and g.isnumeric():
    ficha(gols=g)
else:
    ficha()
