def leiaDinheiro(msg):
    valido = False
    while not valido:
        valor = str(input(f'{msg}')).strip().replace(',','.')
        if valor.isalpha() or valor == '':
            print(f'\033[0;31mO valor \"{valor}\" é inválido... Digite novamente!!!\033[m')
        else:
            valido = True
            return float(valor)
            break