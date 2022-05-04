qtde_mulheres_novas = 0
idade_homem_velho = 0
idade_total = 0
for c in range(1, 4+1):
    print('----- {}ª PESSOA -----'.format(c))
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    idade_total += idade
    if sexo == 'M':
        if idade > idade_homem_velho:
            idade_homem_velho = idade
            nome_homem_velho = nome
    else:
        if idade < 20:
            qtde_mulheres_novas += 1
print('---- FIM ----')
media_idade = idade_total / 4
print('''Média de idade do grupo: {}
Homem mais velho: {}
Mulheres abaixo de 20 anos: {}'''.format(media_idade, nome_homem_velho, qtde_mulheres_novas))