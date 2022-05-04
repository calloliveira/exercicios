n = int(input('Digite um número: '))
print('='*12)
print('TABUADA')
print('=' * 12)
for c in range(1, 10+1):
    print('{} x {} = {}'.format(n, c, n * c))
print('=' * 12)
