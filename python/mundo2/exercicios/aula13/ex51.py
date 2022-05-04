termo = int(input('Digite o termo da PA: '))
razao = int(input('Digite a razão da PA: '))
soma = 0
termo_atual = termo
print('{}'.format(termo), end=' -> ')
for c in range(1, 10):
    soma = razao + termo_atual
    print(soma, end=' -> ')
    termo_atual = termo_atual + razao
print('FIM')