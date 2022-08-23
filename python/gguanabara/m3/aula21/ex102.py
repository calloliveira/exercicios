def fatorial(num, show=False):
    """
    -> Calcula o fatorial do número informado
    :param num: número a ser calculado o fatorial
    :param show: parametro opcional para exibir ou não o processo de cálculo
    :return: Retorna o valor do cálculo de num
    """
    fact = 1
    for c in range(num, 0, -1):
        if show:
            print(c, end=' ')
            if c > 1:
                print('x', end=' ')
            else:
                print('=', end=' ')
        fact *= c
    return fact


#Programa principal
print(fatorial(5))
help(fatorial)
