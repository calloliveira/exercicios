def voto(anonasc):
    from datetime import date
    anoatual = date.today().year
    idade = anoatual - anonasc
    if idade < 16:
        return f'COM {idade} ANOS, VOCÊ AINDA NÃO PODE VOTAR!!!'
    elif idade >= 18 and idade < 70:
        return f'COM {idade} ANOS, O VOTO É OBRIGATÓRIO!!!'
    else:
        return f'COM {idade} ANOS, O VOTO É OPCIONAL!!!'


#Programa principal        
anonasc = int(input('Qual o seu ano de nascimento? '))
print(voto(anonasc))