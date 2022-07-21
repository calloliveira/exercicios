geral = dict()
tot = 0
media = 0
geral["Nome"] = str(input('Qual o nome do jogador? '))
geral["Qtd_Partidas"] = int(input('Qual a quantidade de partidas jogadas? '))
for c in range(0, geral["Qtd_Partidas"]):
    geral[f"Partida {c+1}"] = int(input(f'Quantidade de gols na partida de Nº {c+1}: '))
    tot += geral[f"Partida {c+1}"]
geral["Total_Gols"] = tot
geral["Media_Gols_Partida"] = tot / geral["Qtd_Partidas"]
print('=-' * 20)
print(f'{"APROVEITAMENTO DO JOGADOR":*^30}')
for k, v in geral.items():
    print(f'{k}: {v}')
print('=-' * 20)