print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR um triângulo ', end='')
    if r1 == r3 == r2:
        print('Equilátero !!!')
    elif r1 == r2 and r1 != r3 or r3 == r1 and r3 != r2 or r2 == r3 and r3 != r1:
        print('Isósceles !!!')
    else:
        print('Escaleno !!!')
else:
    print('Os segmentos acima NÃO PODEM FORMAR Triângulos !!!')