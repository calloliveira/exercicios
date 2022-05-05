from datetime import date
nasc = int(input('Digite o ano de nascimento do atleta: '))
idade = date.today().year - nasc
print('O atleta tem {} anos.'.format(idade))
if idade <= 9:
    print('Classificação: MIRIM !!!')
elif idade <= 14:
    print('Cassificação: INFANTIL !!!')
elif idade <= 19:
    print('Classificação: JUNIOR !!!')
elif idade <= 25:
    print('Classificação: SENIOR !!!')
else:
    print('Classificação: MASTER !!!')