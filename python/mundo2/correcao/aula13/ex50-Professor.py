soma = 0
cont = 0
for c in range(0, 6):
    num = int(input('Digite um número: '))
    if num % 2 == 0:
        soma += 1
        cont += 1
print('O valor da soma entre os {} números pares digitados é {}'.format(cont, soma))