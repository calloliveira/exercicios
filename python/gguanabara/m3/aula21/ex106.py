c = ('\033[m', # 0 - Sem cores
    '\033[0;30;41m', # 1 - Vermelho
    '\033')

def ajuda(com):
    help(com)

def título(msg, cor=0):
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}  ')
    print('~' * tam)
    print(c[0], end='')


#Program principal
comando = ''
while True:
    título('SISTEMA DE AJUDA PyHELP', 1)
    comando = str(input("Função ou biblioteca > "))
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
título('ATÉ LOGO')