# Escreva um programa que leia o salário de um funcionário,
# e calcule o valor do seu aumento.
# Para salários superiores a R$ 1.250,-- calcule um aumento de 10%,
# Para os inferiores ou iguais, o aumento é de 15%
'''Carlos
salario = float(input('Digite o seu salário atual: '))
if salario <= 1250.00:
    print('Seu salário de R$ {:.2f}, com aumento de 15%, passa a ser de R$ {:.2f}'.format(salario, (salario*15)/100+salario))
else:
    print('Seu salário de R$ {:.2f}, com aumento de 10%, passa a ser de R$ {:.2f}'.format(salario, (salario*10)/100+salario))
'''

'''Professor'''
salário = float(input('Qual é o salário do funcionário? '))
if salário <= 1250:
    novo = salário + (salário * 15 / 100)
else:
    novo = salário + (salário * 10 / 100)
print('Quem ganhava R${:.2f} passa a ganhar R${:.2f}'.format(salário, novo))
