''' Carlos '''

from datetime import date
print('[1] - Homem')
print('[2] - Mulher')
option = int(input('Digite a opcao - '))
if option == 1:
    nasc = int(input('Qual é o seu ano de nascimento? '))
    alist = date.today().year - nasc
    if alist == 18:
        print('Está na hora de se alistar no exército brasileiro !!!')
    elif alist < 18:
        tempo_falt = 18 - alist
        print('Você ainda não tem idade o suficiente para se alistar, faltam {} anos !!!'.format(tempo_falt))
    else:
        temp_exc = alist - 18
        print('Já passou da hora de se alistar no exército brasileiro. Você está atrasado {} anos !!!'.format(temp_exc))
else:
    print('Você é uma dama, não precisa se alistar !!!')


'''Professor

from datetime import date
atual = date.today().year
nasc = int(input('Qual é o seu ano de nascimento? '))
idade = atual - nasc
print('Quem nasceu em {} tem {} anos'.format(nasc, idade))
if idade == 18:
    print('Você tem que se alistar IMEDIATAMENTE !!!')
elif idade < 18:
    saldo = 18 - idade
    print('Ainda faltam {} anos para o seu alistamento !!!'.format(saldo))
    ano = atual + saldo
    print('Seu alistamento será em {}'.format(ano))
elif idade > 18:
    saldo = idade - 18
    print('Você já deveria ter se alistado a {} anos !!!'.format(saldo))
    ano = atual - saldo
    print('Seu alistamento foi em {}'.format(ano))

'''