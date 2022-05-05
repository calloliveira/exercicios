# Faça um algoritmo que leia o preço de um produto e mostre o seu preço
# com 5% de desconto

p = float(input('Digite o valor do produto: R$ '))

print('O valor do produto com desconto é: R$ {:.2f}'.format((p/100)*95)) #Método Carlos
print('O valor do produto com desconto é: R$ {:.2f}'.format(p-(p*5/100))) #Método Professor