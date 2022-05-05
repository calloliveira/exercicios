frase = str(input('Digite uma frase: ')).lower()
frase = frase.replace(" ", "")
new_frase = frase[::-1]
print(new_frase)
if frase == new_frase:
    print('Esta frase É UM PALÍNDROMO !!!')
else:
    print('Esta frase é NÃO UM PALÍNDROMO !!!')
