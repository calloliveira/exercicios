sexo = ''
while sexo != 'M' and sexo != 'F':
    sexo = str(input('Digite o sexo [M/F]: '))
    if sexo != 'M' and sexo != 'F':
        print('Sexo inválido !!!')