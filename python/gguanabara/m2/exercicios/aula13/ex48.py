soma = 0
for c in range(1, 501):
    if c % 2 != 0 and c % 3 == 0:
        print('Contador: {} | Soma: {}'.format(c, soma))
        soma = soma + c
print('A soma do total entre os múltiplos de 3 é {}'.format(soma))