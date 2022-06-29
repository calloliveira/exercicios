aluno = list()
boletim = list()
c = 0
while True:
    aluno.append(str(input('Digite o nome do aluno: ')).upper())
    aluno.append(float(input('Digite a primeira nota: ')))
    aluno.append(float(input('Digite a segunda nota: ')))
    boletim.append(aluno[:])
    cont = str(input('Deseja continuar [S/N] ? '))
    aluno.clear()
    if cont in 'Nn':
        break
print('=-' * 30)
print('BOLETIM DA CLASSE')
print('=-' * 30)
print(f'{"NOME":-<20}MÉDIA', end='')
print()
for a in boletim:
    media = (a[1] + a[2]) / 2
    print(f'{a[0]:.<20}', end='')
    print(f'{media}')
print()    
while True:
    pesquisa = str(input('Pesquisar Aluno ou 999 P/ Sair: ')).upper()
    if pesquisa == '999':
        break
    for a in boletim:
        if a[0] == pesquisa:
            media = (a[1] + a[2]) / 2
            aluno.clear()
            aluno = a[0:]       
    if not aluno == []:
        print(f'Aluno: {aluno[0]} | N1: {aluno[1]} | N2: {aluno[2]} | Média: {media}')
        aluno.clear()
        print()
    else:
        print(f'O Aluno {pesquisa} não foi encontrado no boletim !!!')
        print()