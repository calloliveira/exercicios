def leiaInt(msg):
    while True:
        num = str(input(msg))
        if num.isnumeric():
            return int(num)
            break
        else:
            print('\033[31mERRO!!! Digite um número válido...\033[m')

 
#Programa principal
valor = leiaInt('Digite um número: ')
print(f'\033[32mVocê digitou o número {valor}\033[m')