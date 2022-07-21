# Desenvolva um programa que pergunte a distância da viagem em KM
# calcule o preço da passagem em KM, cobrando R$ 0,50 por KM para
# viagens de até 300km, e R$ 0.45 para viagens mais longas.

'''Carlos
dist = float(input('Digite a distância da viagem: '))
if dist <= 300:
    print('O preço da passagem é de R$ {:.2f}'.format(dist*0.50))
else:
    print('O valor da passagem é de R$ {:.2f}'.format(dist*0.45))
'''

'''Professor (Método 1)
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distância))
if distância <= 200:
    preço = distância * 0.50
else:
    preço = distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))
'''

'''Professor (Método 2)'''
distância = float(input('Qual é a distância da sua viagem? '))
print('Você está prestes a começar uma viagem de {}Km'.format(distância))
preço = distância * 0.50 if distância <= 200 else distância * 0.45
print('E o preço da sua passagem será de R${:.2f}'.format(preço))