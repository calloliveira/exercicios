n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('Você foi reprovado, pois a sua média é inferior a 5 !!!'.format(media))
elif media > 5 and media <= 6.9:
    print('Você está de recuperação, pois a sua média é inferior a 7 !!!')
else:
    print('Parabéns, você foi aprovado com uma média de {}'.format(media))
