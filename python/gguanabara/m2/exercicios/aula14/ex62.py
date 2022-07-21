print('Gerador de PA')
print('-=' * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Razão da PA: '))
termo = primeiro
cont = 1
termoscont = 10
totermos = 0
while cont <= termoscont:
    print('{} -> '.format(termo), end='')
    termo += razão
    cont += 1
    if cont > termoscont:
        totermos += termoscont
        print('FIM')
        quest = int(input('Deseja exibir quantos termos adicionais? '))
        if quest != 0:
            termoscont = quest
            cont = 1
print('Você exibiu {} termos!'.format(totermos))       
