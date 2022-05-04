núm = (int(input('Digite um número: ')),
       int(input('Digite outro número: ')),
       int(input('Digite mais um número: ')),
       int(input('Digite o último número: ')))
print(f'Voce digitou os valores {núm}')
print(f'O valor 9 apareceu {núm.count(9)} vez(es)')
if 3 in núm:
    print(f'O valor 3 apareceu na {núm.index(3)+1}ª posição')
else:
    print('O valor 3 não foi digitado')
print('Os valor pares digitados foram: ', end='')
for count in núm:
    if count % 2 == 0:
        print(count, end=' ')
        