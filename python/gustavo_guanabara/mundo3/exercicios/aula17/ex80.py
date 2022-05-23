valores = list()
for cont in range (0,5):
    valor = int(input('Digite um valor: '))
    if valores == [] or valor > valores[-1]:
        valores.append(valor)
    else:
        pos = 0
        while pos < len(valores):
            if valor < valores[pos]:
                valores.insert(pos, valor)
                break
            pos += 1
print(valores)