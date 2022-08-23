def notas(*notas, sit=False):
    """
    -> Função para analisar a nota de vários alunos
    :param n: indica uma ou mais notas
    :param sit: indica a situação de acordo com a média
    :return: retorna o boletim
    """
    boletim = dict()
    boletim['Total_Notas'] = len(notas)
    boletim['Maior_Nota'] = max(notas)
    boletim['Menor_Nota'] = min(notas)
    boletim['Media'] = sum(notas) / len(notas)
    if sit == True:
        if boletim['Media'] >= 5 and boletim['Media'] < 7:
            boletim['Situação'] = 'Razoável'
        elif boletim['Media'] < 5:
            boletim['Situação'] = 'Ruim'
        else:
            boletim['Situação'] = 'Boa'


    
    return boletim


#Programa principal
resp = notas(7, 7, 3, 8, 10, sit=True)
print(resp)
help(notas)