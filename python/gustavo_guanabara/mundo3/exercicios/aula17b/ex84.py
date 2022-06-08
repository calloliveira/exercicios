pessoas = list()
tot = 0
pesadas = []
leves = []
continua = 'null'
#Leitura dos dados
while True:
    nome = str(input('Digite o nome: '))
    peso = float(input('Digite o peso: '))
    pessoas.append([nome, peso])
    while not continua in 'SNsn':
        continua = str(input('Deseja continuar? [S/N] '))
    if continua in 'Nn':
        break
    else:
        continua = 'null'
#Tratamento dos dados  
for p in pessoas:
    tot += 1
    if pesadas == [] and leves == []:
        pesadas.append(p)
        leves.append(p)
    elif p[1] > pesadas[0][1]:
        pesadas.clear()
        pesadas.append(p)
    elif p[1] < leves[0][1] :
        leves.clear()
        leves.append(p)
        

print(f'Total de pessoas cadastradas: {tot}')
print(f'Pessoas mais pesadas {pesadas}')
print(f'Pessoas mais leves {leves}')