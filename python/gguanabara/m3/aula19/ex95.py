jogadores = []
geral = dict()
cont = 'null'
print('=-' * 25)
print(f'{"CADASTRO DE JOGADORES":-^50}')
print('=-' * 25)
while True:
    tot = 0
    media = 0
    geral["Nome"] = str(input('Qual o nome do jogador? '))
    geral["Partidas"] = int(input('Qual a quantidade de partidas jogadas? '))
    for c in range(0, geral["Partidas"]):
        geral[f"Partida {c+1}"] = int(input(f'Quantidade de gols na partida de Nº {c+1}: '))
        tot += geral[f"Partida {c+1}"]
    geral["Total_Gols"] = tot
    geral["Media_Gols_Partida"] = tot / geral["Partidas"]
    jogadores.append(geral.copy())
    geral.clear()
    print('=-' * 25)
    cont = str(input('Deseja cadastrar mais jogadores? [S/N] '))
    print('=-' * 25)
    if cont in 'Nn':
        break
print('=-' * 25)
print(f'{"PESQUISAR JOGADORES":-^50}')
print('=-' * 25)
while True:
    jogname = str(input('Exibir detalhes do jogador: '))
    for j in jogadores:
        if jogname == j["Nome"]:
            for k, v in j.items():
                print(f'{k}: {v}')
    print('=-' * 25)
    cont = str(input('Deseja continuar? [S/N] '))
    print('=-' * 25)
    if cont in 'Nn':
        break
print(f'{"PROGRAMA FINALIZADO":-^50}')
print('=-' * 25)