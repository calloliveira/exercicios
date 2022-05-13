opt = 'null'
while True:
    status = ['Em uso', 'Doacao', 'Roubo/Furto', 'Obsoleto/Descarte', 
          'Onboarding', 'Rollout', 'Aguardando-Doacao', 
          'Aguardando-Devolucao', 'Emprestimo', 'Quarentena', 'Backup', 'Manutencao'] 
    print('-' * 20)
    print('Escolha a opção')
    print('-' * 20, '\n')    
    for s in status:
        print(f'Status: {s}')
    while not opt in status:
        opt = str(input('\nDigite a sua opção: '))
    print('\n')
    print('-' * 20)
    print('LISTAGEM ORDENADA')
    print('-' * 20, '\n')
    print(f'\nStatus: {opt}')
    for s2 in status:
        if not opt == s2:
            print(f'Status: {s2}')
    cont = 'null'
    opt = 'null'
    if cont not in 'SsNn':
        cont = str(input('\nDeseja continuar? [S/N] '))
    if cont in 'Nn':
        break
    