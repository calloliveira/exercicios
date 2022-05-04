total = maismil = prodprecobarato = 0
prodnomebarato = '' 
while True:
    nome_produto = str(input('Digite o nome do produto: '))
    preço = float(input('Digite o preço do produto: R$ '))
    total += preço
    if preço > 1000:
        maismil += 1
    if prodnomebarato == '' and prodprecobarato == 0:
        prodnomebarato = nome_produto
        prodprecobarato = preço
    if preço < prodprecobarato:
        prodnomebarato = nome_produto
    continua = str(input('Deseja continuar? [S/N] '))
    while not continua in 'NnSs':
        continua = str(input('Deseja continuar? [S/N] '))
    if continua in 'Nn':
        break
print(f'''
      Você gastou um total de R$ {total:.2f}
      {maismil} Produtos acima de R$ 1000,00
      O produto mais barato foi {prodnomebarato} que custa R$ {prodprecobarato}
      ''')