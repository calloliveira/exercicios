dados = list()
pessoas = list()
pesadas = []
leves = []
continua = 'null'
#Leitura dos dados
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    pessoas.append(dados[:])
    dados.clear()
    while not continua in 'SNsn':
        continua = str(input('Deseja continuar? [S/N] '))   
    if continua in 'Nn':
        break
    else:
        continua = 'null'
#Tratamento dos dados  
for p in pessoas:
    if pesadas == [] and leves == []:
        pesadas.append(p)
        leves.append(p)
    elif p[1] > pesadas[0][1]:
        pesadas.clear()
        pesadas.append(p)
    elif p[1] == pesadas[0][1]:
        pesadas.append(p)
    elif p[1] < leves[0][1] :
        leves.clear()
        leves.append(p)
    elif p[1] == leves[0][1] :
        leves.append(p)
print('=-' * 30)
print(f'Total de pessoas cadastradas: {len(pessoas)}')
print('=-' * 30)
print(f'Pessoas mais pesadas: ')
for p in pesadas:
    print(f'{p[0]} - {p[1]} KGs')
print('=-' * 30)
print(f'Pessoas mais leves: ')
for p in leves:
    print(f'{p[0]} - {p[1]} KGs')