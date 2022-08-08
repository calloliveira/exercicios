def maior(lista_num):
    maior = 0
    for n in lista_num:
        if n > maior:
            maior = n
    print(f'O maior valor digitado foi {maior}')

valores = []
while True:
    num = int(input('Digite um valor [999 Stop]: '))
    if num == 999:
        break
    valores.append(num)
maior(valores)

