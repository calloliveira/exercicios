pd = pe = 0
exp = str(input('Digite uma expressão numérica: '))
for v in exp:
    if v == "(":
        pd += 1
    if v == ")":
        pe += 1
if pd == pe:
    print('Sua expressão é válida !!!')
else:
    print('Sua expressão é inválida')