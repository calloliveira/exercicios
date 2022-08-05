def escreva(msg):
    tamanho = len(msg)
    print("=" * (len(msg) + 4))
    print(f'  {msg}  ')
    print("=" * (len(msg) + 4))


frase = str(input('Digite uma mensagem: '))
escreva(frase)