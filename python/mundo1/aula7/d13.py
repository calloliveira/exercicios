# Faça um algoritmo que leia o salário de um funcionáro e mostre o seu
# novo salário, com 15% de aumento

s = float(input('Salário atual: R$ '))

print('Salário com aumento: R$ {:.2f}'.format(s*0.15+s)) #Método Carlos
print('Salário com aumento: R$ {:.2f}'.format(s+(s*15/100))) #Método Carlos