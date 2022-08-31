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