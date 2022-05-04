num = int(input('Quantos termos deseja exibir? '))
c = 1
while c < num:
    if c == 1:
        anterior = 1
        atual = 1
        fibo = anterior + atual
        print('0->{}->{}->{}'.format(anterior, atual, fibo), end='->')
        c += 3
    else:
        anterior = atual
        atual = fibo
        fibo = atual + anterior
        print('{}'.format(fibo), end='->')
        c += 1
print('FIM')
