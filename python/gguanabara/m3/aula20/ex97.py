def escreva(msg):
    print("=" * (len(msg) + 4))
    print(f'  {msg}  ')
    print("=" * (len(msg) + 4))


#Programa principal
frase = str(input('Digite uma mensagem: '))
escreva(frase)