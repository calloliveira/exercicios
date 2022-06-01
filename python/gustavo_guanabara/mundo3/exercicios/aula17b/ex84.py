pessoas = list()
tot = 0
pesadas = []
leves = []
#Leitura dos dados
while True:
    nome = str(input('Digite o nome: '))
    peso = int(input('Digite o peso: '))
    pessoas.append([nome, peso])
    continua = str(input('Deseja continuar? [S/N] '))
    if continua in 'Nn':
        break
#Tratamento dos dados  
for i, p in enumerate(pessoas):
    tot += 1
    if pesadas == [] and leves == []:
        pesadas.append(p)
        leves.append(p)
    if p[1] > pesadas[0][1]:
        pesadas.clear()
        pesadas.append(p)
    elif peso == pesadas[0][1]:
        pesadas.append(p)
    elif p[1] < leves[0][1]:
        leves.append(p)
    
       
print(f'Total de pessoas cadastradas: {tot}')
print(f'Pessoas mais pesadas {pesadas}')
print(f'Pessoas mais leves {leves}')