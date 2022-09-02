def aumentar(num, p, show=False):
    res = p * (num / 100)
    return res if show is False else moeda(res)

def diminuir(num, p, show=False):
    res = num - ((num / 100) * p)
    return res if show is False else moeda(res)


def dobro(num=0, show=False):
    res = num * 2
    return res if show is False else moeda(res)

def metade(num=0, show=False):
    res = num / 2
    return res if show is False else moeda(res)

def moeda(v, moeda='R$'):
    return f'{moeda} {v:.2f}'.replace('.',',')


def resumo(num, pmais, pmenos):
    print('-' * 35)
    print('RESUMO DO VALOR'.center(35))
    print('-' * 35)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num, True)}')
    print(f'{pmais}% de aumento: \t{aumentar(num, pmais, True)}')
    print(f'{pmenos}% de reduçao: \t{diminuir(num, pmenos, True)}')
    print('-' * 35)