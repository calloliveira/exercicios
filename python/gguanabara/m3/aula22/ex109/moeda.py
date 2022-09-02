def aumentar(num, p, show=False):
    res = num + ((num / 100) * p)
    return res if show is False else moeda(res)


def diminuir(num, p, show=False):
    res = num - ((num / 100) * p)
    return res if show is False else moeda(res)


def dobro(num, show=False):
    res = num * 2
    return res if show is False else moeda(res)


def metade(num, show=False):
    res = num / 2
    return res if show is False else moeda(res)
    
def moeda(v):
    return f'R$ {v}'