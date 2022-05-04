# Escreva um programa que leia a velocida de um carro
# Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
# A multa vai custar R$ 7,00 por cada km acima do limite.


''' Carlos
velox = int(input('Qual a velocidade do veículo? '))
if velox > 80:
    print('Você foi multado !!!\n O valor de sua multa é de R$ {:.2f}'.format((velox-80)*7))
else:
    print('Velocida permitida, sem penalidade ao condultor !!!')
'''

'''Professor'''
velocidade = float(input('Qual é a velocidade atual do carro? '))
if velocidade > 80:
    print('MULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!'.format(multa))
print('Tenha um bom dia! Dirija com segurança')

