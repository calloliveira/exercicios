num = int(0)
c = 0
total = 0
while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if not num == 999:
        total += num
        c += 1
print('Você digitou {} números, e a soma entre eles é {}'.format(c, total))
