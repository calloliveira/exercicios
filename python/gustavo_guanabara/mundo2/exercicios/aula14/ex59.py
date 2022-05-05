opcao = 0
while opcao != 5:
    n1 = int(input('Digite um número: '))
    n2 = int(input('Digite outro número: '))
    print('''
          [1] - Somar
          [2] - Multiplicar
          [3] - Maior & Menor
          [4] - Novos números
          [5] - Sair
          ''')
    opcao = int(input('Escolha a opção:'))
    if opcao == 1:
        print('Você escolheu a operação de soma !!!')
        soma = n1 + n2
        print('{} + {} = {}'.format(n1, n2, soma))
    elif opcao == 2:
        print('Você escolheu a operação de multiplicação !!!')
        mult = n1 * n2
        print('{} x {} = {} '.format(n1, n2, mult))
    elif opcao == 3:
        print('Você escolheu a operação de maior & menor !!!')
        if n1 > n2:
            maior = n1
            menor = n2
        else:
            maior = n2
            menor = n1
        print('Maior: {} | Menor: {}'.format(maior, menor))
    elif opcao == 4:
        print('Você escolheu novos números !!!\n')
    elif opcao == 5:
        print('Você escolheu SAIR !!!')
    else:
        print('OPÇÃO INVÁLIDA!!! ')
