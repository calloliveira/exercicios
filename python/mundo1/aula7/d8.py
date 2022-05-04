# Escreva um programa que leia um valor em metros e o exiba
# convertido em centímetros e milímetros.

n = float(input('Digite o valor em metros: '))

print('\n{:=^30}'.format('Múltiplos do metro'))
print('\n{} Metro(s) equivale(m) a:\n'.format(n))
print('{} - KMs\nHMs: {}\nDAMs: {}\n'.format(n/1000, n/100, n/10))
print('{:=^30}'.format('Sub-Mútiplos do metro'))
print('\n{} Metro(s) equivale(m) a:\n'.format(n))
print('CMs: {:.0f}\nMMs: {:.0f}'.format(n*100, n*1000))