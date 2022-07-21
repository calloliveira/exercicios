while True:
    num = int(input('Digite um número [< 0 para parar]: '))
    print('-' * 30)
    if num < 0:
        break
    for c in range(1,11):
        print(f'{num} X {c} = {num * c} ')
    print('-' * 30)
print('Programa finalizado!!!')