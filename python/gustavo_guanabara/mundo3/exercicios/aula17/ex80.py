valores = list()
for cont in range (0, 5):
    valor = int(input('Digite um valor: '))
    if valores == []:
        valores.append(valor)
    else:
        if valor > valores[cont-1]:
            valores.append(valor)
        else:
            valores.insert(valores[cont-1], valor)
            print('Deu certo 2')
print(valores)