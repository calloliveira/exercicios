while True:
    status = ['Em uso', 'Doacao', 'Roubo/Furto', 'Obsoleto/Descarte', 
          'Onboarding', 'Rollout', 'Aguardando-Doacao', 
          'Aguardando-Devolucao', 'Emprestimo', 'Quarentena', 'Backup', 'Manutencao'] 
    print('Escolha a opção\n')
    for s in status:
        print(f'Status: {s}')
    opt = str(input('\nDigite a sua opção: '))
    print(f'\nStatus: {opt}')
    if opt in status:
        for s2 in status:
            if not opt == s2:
                print(f'Status: {s2}')
