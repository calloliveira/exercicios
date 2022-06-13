boletim = list()
c = 0
while True:
    nome = str(input('Digite o nome do aluno: '))
    nota1 = int(input('Digite a Nota 1: '))
    nota2 = int(input('Digite a Nota 2: '))
    boletim[c].append([nome, nota1, nota2])
    cont = str(input('Deseja continuar [S/N] ? '))
    if cont in 'Nn':
        break
    c += 1
print(boletim)