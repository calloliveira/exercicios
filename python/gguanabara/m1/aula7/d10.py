# Crie um programaa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar
# Considere US$1,00 == R$ 3,27

din = float(input('Quanto de dinheiro você tem na carteira? '))

print('Com R$ {} você pode comprar US$ {:.2f} !!!'.format(din, din/3.27))