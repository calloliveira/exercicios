def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO!!! Digite um número inteiro válido...\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO!!! O usuário preferiu não digitar o valor...\033[m')
            return 0
        else:
            return num

def leiaFloat(msg):
    while True:
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mERRO!!! Digite um número real válido...\033[m')
            continue
        except (KeyboardInterrupt):
            print('\033[31mERRO!!! O usuário preferiu não digitar o valor...\033[m')
            return 0
        else:
            return num


# Programa principal
inum = leiaInt('Digite um número inteiro:  ')
fnum = leiaFloat('Digite um número real: ')
print(f'\033[32mVocê digitou os números {inum} & {fnum}\033[m')