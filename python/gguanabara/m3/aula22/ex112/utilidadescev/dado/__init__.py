def leaiDinheiro(msg):
    while True:
        valor = str(input(f'{msg}'))
        if valor.isnumeric():
            return float(valor)
            break
        else:
            print(f'\033[0;31mO valor {valor} é inválido... Digite novamente!!!\033[m')
        