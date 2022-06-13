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
for a in boletim:
    print(f'Aluno: {a[0]} Nota1: {a[1]} Nota2: {a[2]} Média: {(a[1] + a[2]) / 2}')