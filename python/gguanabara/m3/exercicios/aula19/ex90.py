aluno = dict()
aluno['Nome'] = str(input('Nome do aluno: '))
aluno['Media'] = float(input(f'Média de {aluno["Nome"]}: '))
if aluno['Media'] <= 5:
    aprov = 'Reprovado'
elif aluno['Media'] >= 7:
    aluno['Situação'] = 'Aprovado'
else:
    aluno['Situação'] = 'Recuperação'
print('-=' * 30)
for k, v in aluno.items():
    print(f'- {k}: {v}')
print('-=' * 30)