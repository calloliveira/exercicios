geral = list()
mulheres = list()
pessoa = dict()
idademediamais = list()
totpessoas = totidade = mediaidade = 0
while True:
    pessoa["Nome"] = str(input('Digite o nome: ')).upper()
    pessoa["Sexo"] = str(input('Digite o sexo [F/M]: ')).upper()
    pessoa["Idade"] = int(input('Digite a idade: '))
    geral.append(pessoa.copy())
    totpessoas += 1
    totidade += pessoa["Idade"]
    if pessoa["Sexo"] == 'F':
        mulheres.append(pessoa.copy())
    cont = str(input('Deseja continuar [S/N]? '))
    if cont in 'Nn':
        break
mediaidade = totidade /totpessoas
for p in geral:
    for k, v in p.items():
        if k == 'Idade' and v > mediaidade:
            idademediamais.append(p.copy())
print(f'\n{"Processamento do cadastro":-^45}')
print(f'\nTotal de pessoas cadastradas: {totpessoas}')
print(f'Média de idade do grupo: {mediaidade:.2f}\n')
print('Mulheres cadastradas:\n')
for m in mulheres:
    for k, v in m.items():
        if not k == 'Sexo':
            print(f'{k}: {v}')
    print('\n')
print('Idade acima da média:\n')
for p in idademediamais:
    for k, v in p.items():
        print(f'{k}: {v}')
    print('\n')
