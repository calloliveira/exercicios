maior = 0
menor = 0
for c in range(1, 5+1):
    peso = float(input('Digite o {}º peso: '.format(c)))
    if peso > maior:
        maior = peso
    elif menor == 0 or peso < menor:
        menor = peso
print('O maior peso digitado foi de {:.2f} KG e o menor de {:.2f} KG'.format(maior, menor))
