valor = float(input('Qual o valor do imóvel? '))
renda = float(input('Qual o valor da sua renda? '))
prazo = int(input('Em quantos anos deseja pagar o imóvel? ')) * 12
parcela = valor / prazo

if parcela <= renda * 0.30:
    print('Seu empréstimo foi aprovado com uma parcela de R${:.2f}, parabéns !!!'.format(parcela))
else:
    print('Seu empréstimo foi negado, pois o valor de R${:.2f}, excede 30% da sua renda de R${:.2f}!!!'.format(parcela, renda))
