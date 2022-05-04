from random import choice
from time import sleep
opt_pc = choice(['Pedra', 'Papel', 'Tesoura'])
print('''
[1] - Pedra
[2] - Papel
[3] - Tesoura
''')
opt_pl = str(input('Qual a sua escolha? '))
print('')
if opt_pl == '1':
    opt_pl = 'Pedra'
elif opt_pl == '2':
    opt_pl = 'Papel'
else:
    opt_pl = 'Tesoura'
print('Aguarde enquanto o resultado é apurado')
print('')
print('')
print('JÓO')
sleep(1)
print('Ken')
sleep(1)
print('Pôo')
sleep(1)
print('')
print('Quem será que ganhou?')
print('')
sleep(2)
if opt_pl == opt_pc:
    print('O computador escolheu {} e você também. EMPATE TÉCNICO !!!'.format(opt_pc))
elif opt_pl == 'Pedra' and opt_pc == 'Tesoura' or opt_pl == 'Papel' and opt_pc == 'Pedra' or opt_pl == 'Tesoura' and opt_pc == 'Papel':
    print('O computador escolheu {}'.format(opt_pc))
    print('Você escolheu {}'.format(opt_pl))
    if opt_pl == 'Pedra' and opt_pc == 'Tesoura':
        print('A pedra quebra a tesoura !!!')
        print('Parabéns, você ganhou !!!')
    elif opt_pl == 'Papel' and opt_pc == 'Pedra':
        print('O papel cobre e sufoca a pedra !!!')
        print('Parabéns, você ganhou !!!')
    else:
        print('A tesoura corta o papel !!!')
        print('Parabéns, você ganhou !!!')
else:
    print('Você perdeu !!!')
    print('O computador escolheu {}'.format(opt_pc))
    print('Você escolheu {}'.format(opt_pl))
    if opt_pc == 'Pedra':
        print('A pedra quebra a tesoura !!!')
    elif opt_pc == 'Tesoura':
        print('A tesoura corta o papel !!!')
    else:
        print('O papel cobre e sufoca a pedra !!!')