#Faça um programa que leia a entrada do teclado e exiba o
# tipo primitivo e todas as informações possíveis sobre o valor digitado

n = input('Digite algo: ')

#Valida tipo variável-----
print('Tipo da variável -', type(n))


#Valida tipo do valor digitado-----
print('Alphanumérico: ', n.isalnum())
print('Numérico: ', n.isnumeric())
print('Letra: ', n.isalpha())
print('Minúsculo: ', n.islower())
print('Maiúsculo: ', n.isupper())


