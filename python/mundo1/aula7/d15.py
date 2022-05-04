#Escreva um programa que pergunte a quantidade de KMs percorridos por um carro alugado
# e a quantidade de dias pelos quais foi alugado. Calcule o preço a pagar, sabendo que o
# carro custa R$ 60 o dia e R$ 0,15 por KM rodado.

dias = int(input('Por quantos dias você usou o carro? '))
km = float(input('Qual a quantidade de KM percorrido? '))
total_dias = dias * 60
total_km = km * 0.15

print('O valor total do serviço de locação é R$ {:.2f}'.format(total_dias+total_km))