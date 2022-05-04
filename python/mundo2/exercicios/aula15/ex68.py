cont = 0
from random import randint
while True:
    print('=-'*15)
    print('Vamos jogar par ou ímpar?')
    print('=-'*15)
    num_jogador = int(input('Digite seu número: '))
    opt_jogador = str(input('Escolha a sua opção [P/I]: ')).upper()
    num_pc = randint(0, 11)
    if opt_jogador == 'P':
        opt_jogador = 'PAR'
        opt_pc = 'ÍMPAR'
    else:
        opt_jogador = 'ÍMPAR'
        opt_pc = 'PAR'   
    tot = num_jogador + num_pc
    if tot % 2 == 0:
        resultado = 'PAR'
    else:
        resultado = 'ÍMPAR'
    if resultado == opt_jogador:
        print(f'Parabéns, você ganhou! O número {tot} é {opt_jogador}')
        cont += 1
    else:
        print('Você perdeu!')
        break
print(f'Você ganhou {cont} vez(es) consecultiva(s)!!!')