def aumentar(num, p):
    return (((num / 100) * p) + num)


def diminuir(num, p):
    return (num - ((num / 100) * p))


def dobro(num):
    return (num * 2)

def metade(num):
    return (num / 2)


def moeda(preço, moeda = 'R$'):
    return f'{moeda}{preço:>.2f}'.replace('.',',')