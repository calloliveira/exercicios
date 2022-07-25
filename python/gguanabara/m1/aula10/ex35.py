# Desenvolva um programa que leia o comprimento de três retas
# e diga ao usuário se elas podem ou não formar um triângulo.
'''Carlos
r1 = int(input('Digite a reta 1: '))
r2 = int(input('Digite a reta 2: '))
r3 = int(input('Digite a reta 3: '))

if r1 > r2 and r1 > r3:
    if r2 + r3 <= r1:
        print('É impossível formar um triângulo com essas medidas !!!')
    else:
        print('É perfeitamente possível formar um triângulo com esses medidas !!!')
if r2 > r3 and r2 > r1:
    if r3 + r1 <= r2:
        print('É impossível formar um triângulo com essas medidas !!!')
    else:
        print('É perfeitamente possível formar um triângulo com essas medidas !!!')
if r3 > r1 and r3 > r2:
    if r1 + r2 <= r3:
        print('É impossível formar um triângulo com essas medidas !!!')
    else:
        print('É perfeitamente possível formar um triângulo com essas medidas !!!')
'''
print('-=' * 20)
print('Analisador de triângulos')
print('-=' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo segmento:'))
r3 = float(input('Terceiro segmento: '))
if r1 < r2 + r3 and r2 < r3 + r1 and r3 < r1 + r2:
    print('Os segmentos acima PODEM FORMAR Triângulos')
else:
    print('Os segmentos acima NÃO PODEM FORMAR Triângulos')