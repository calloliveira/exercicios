from urllib import request, error

def validaSite():
    try:
        request.urlopen('http://www.pudim.com.br')
    except(error.URLError):
        return print('O site não está acessível.')
    else:
        return print('O site está acessível.')
    finally:
        print('Acesso finalizado!!!')


#Program principal
validaSite()