from time import sleep
print('*'*5+' Calculadora de IMC '+'*'*5)
print('')
peso = float(input('Digite o seu peso em KG: '))
altura = float(input('Digite a sua altura em MTs: '))
imc = peso / (altura ** 2)
print('')
print('*'*5+' Aguarde enquanto calculamos a situação da sua saúde '+'*'*5)
print('')
sleep(3)
if imc < 18.5:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('Você está ABAIXO do peso IDEAL  !!!')
elif imc < 25:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('Você está no seu peso IDEAL')
elif imc < 30:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('Você está com SOBREPESO')
elif imc < 40:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('Você está com OBESIDADE NÍVEL I, faça uma dieta para melhorar a sua saúde !!!')
else:
    print('Seu IMC é de {:.1f}'.format(imc))
    print('Cuidado, você está com OBESIDADE MÓRBIDA, faça uma cirurgia bariátrica !!!')
