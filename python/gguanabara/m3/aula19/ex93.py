geral = dict()
GolsPartidas = list()
tot = 0
media = 0
geral["Nome"] = str(input('Qual o nome do jogador? '))
geral["Qtd_Partidas"] = int(input('Qual a quantidade de partidas jogadas? '))
for c in range(0, geral["Qtd_Partidas"]):
    gols = int(input(f'Quantidade de gols na partida de Nº {c+1}: '))
    GolsPartidas.append(gols)
    tot += gols
geral["Gols"] = GolsPartidas[:]
geral["Total_Gols"] = tot
geral["Media_Gols_Partida"] = tot / geral["Qtd_Partidas"]
print('=-' * 20)
print(f'{"APROVEITAMENTO DO JOGADOR":*^30}')
print('=-' * 20)
print(geral)
print('=-' * 20)
for k, v in geral.items():
    print(f'{k}: {v}')
print('=-' * 20)
print(f'O jogador {geral["Nome"]} jogou {geral["Qtd_Partidas"]} partidas.')
for i, g in enumerate(geral["Gols"]):
    print(f' => Na partida {i} fez {g} gol(s)')
print(f'Fez um total de {tot} gols!!!')
print('=-' * 20)