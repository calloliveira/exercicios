aluno = list()
boletim = list()
c = 0
while True:
    aluno.append(str(input('Digite o nome do aluno: ')))
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
print(f'{"NOME":-<20}', end='')
print(f'{"NOTA1":-<10}', end='')
print(f'{"NOTA2":-<10}', end='')
print(f'{"MÉDIA"}')
print()
for a in boletim:
    media = (a[1] + a[2]) / 2
    print(f'{a[0]:.<20}', end='')
    print(f'{a[1]:.<10}', end='')
    print(f'{a[2]:.<10}', end='')
    print(f'{media}')

    
    
    