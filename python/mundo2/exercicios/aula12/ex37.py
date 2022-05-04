'''Carlos

num = int(input('Digite um número inteiro qualquer: '))
print('¬¬--'*20)
print('Sistema de conversão de base inteira')
print('¬¬--'*20)
print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')
print('¬¬--'*20)
opcao = int(input('Para qual base deseja realizar a conversão? '))
if opcao == 1:
    num_bin = format(num, 'b')
    print(num_bin)
elif opcao == 2:
    num_octa = format(num, 'o')
    print(num_octa)
else:
    num_hex = format(num, 'x')
    print(num_hex)

'''

'''Professor'''

num = int(input('Digite um número inteiro qualquer: '))
print('¬¬--'*20)
print('Sistema de conversão de base inteira')
print('¬¬--'*20)
print('1 para binário')
print('2 para octal')
print('3 para hexadecimal')
print('¬¬--'*20)
opcao = int(input('Para qual base deseja realizar a conversão? '))
if opcao == 1:
    print ('{} convertido para binário é igual a {}'.format(num, bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para octal é igual a {}'.format(num, oct(num)[2:]))
else:
    print('{} convertido para hexadecimal é {}'.format(num, hex(num)[2:]))