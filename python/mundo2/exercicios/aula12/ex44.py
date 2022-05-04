valor = float(input('Digite o valor do produto: '))
print(''' >>>>> FORMAS DE PAGAMENTO <<<<<
[1] - A vista com dinheiro ou cheque / 10% de desconto
[2] - A vista no crédito / 5% de desconto
[3] - 2x no crédito / Preço normal sem acréscimo
[4] - 3x ou mais no crédito / 20% de acréscimo''')
print('')
pagto = int(input('Digite a opção para pagamento: '))
print('')
if pagto == 1:
    desconto = valor * 0.10
    valor = valor - (valor * 0.10)
    print('Você obteve R$ {} de desconto que equivale a 10% do valor da compra'.format(desconto))
elif pagto == 2:
    desconto = valor * 0.05
    valor = valor - (valor * 0.05)
    print('Você obteve R$ {} de desconto que equivale a 5% do valor da compra'.format(desconto))
elif pagto == 3:
    parcelas = valor / 2
    print('2 X R$ {} SEM JUROS !!!'.format(parcelas))
else:
    valor = valor + (valor * 0.2)
    qtde_parcelas = int(input('Qual a quantidade de parcelas? '))
    parcelas = valor / qtde_parcelas
    print('{} x R$ {}'.format(qtde_parcelas, parcelas))
print('O valor total da sua compra é de R$ {}'.format(valor))