valores = list()
for cont in range (0, 5):
    valor = int(input('Digite um valor: '))
    if valores == []:
        valores.append(valor)
    else:
        for v in valores:
            if valor > v:
                valores.append(valor)
            else:
                print('É NÓIS!!!')        
print(valores)