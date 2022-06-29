aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Media'] = float(input('Média do aluno: '))
if aluno['Media'] < 6:
    aprov = 'Reprovado'
else:
    aprov = 'Aprovado'
aluno['Situação'] = aprov
for k, v in aluno.items():
    print(f'{k} é igual a {v}')