c = idademaior = idademulher = sexohomem = 0
sexo = continua = ''
while True:
    c += 1
    sexo = str(input(f'Digite o {c}º sexo [M/F]: ')).upper()
    while not sexo in 'MmFf':
        sexo = str(input(f'Digite o {c}º sexo [M/F]: ')).upper()
    idade = int(input(f'Digite a {c}ª idade: '))
    if idade >= 18:
        idademaior += 1
    if sexo in 'Mm':
        sexohomem += 1
    if sexo in 'Ff':
        if idade < 20:
            idademulher += 1
    continua = str(input('Deseja continuar? [S/N] '))
    while not continua in 'SsNn':
        continua = str(input('Deseja continuar? [S/N] '))
    if continua in 'Nn':
        break
print(f'''Você cadastrou:\n
      {idademaior} Pessoas com mais de 18 anos;
      {sexohomem} Homens;
      {idademulher} Mulher(es) com menos de 20 anos;
      ''')