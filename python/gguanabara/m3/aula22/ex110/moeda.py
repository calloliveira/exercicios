def aumentar(num, p, show=False):
    if show:
        return f'R$ {((num / 100) * p) + num}'
    else:
        return ((num / 100) * p) + num


def diminuir(num, p, show=False):
    if show:
        return f'R$ {num - ((num / 100) * p)}'
    else:
        return num - ((num / 100) * p)


def dobro(num, show=False):
    if show:
        return f'R$ {num * 2}'
    else:
        return num * 2


def metade(num, show=False):
    if show:
        return f'R$ {num / 2}'
    else:
        return num / 2

def moeda(v):
    return f'R$ {v}'


def resumo(pinput, pmais, pmenos):
    print('-' * 35)
    print(f'{"RESUMO DO VALOR":^35}')
    print('-' * 35)
    print(f'Preço analisado:       R$ {pinput:.2f}')
    print(f'Dobro do preço:        R$ {dobro(pinput):.2f}')
    print(f'Metade do preço:       R$ {metade(pinput):.2f}')
    print(f'{pmais}% de aumento:        R$ {aumentar(pinput, pmais):.2f}')
    print(f'{pmenos}% de reduçao:        R$ {diminuir(pinput, pmenos):.2f}')
    print('-' * 35)