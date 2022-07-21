from datetime import date
dtatual = date.today().year
maior = 0
menor = 0
for c in range(1, 7+1):
    nasc = int(input('Em que ano a {}ª pessoa nasceu? '.format(c)))
    if dtatual - nasc >= 21:
        maior = maior + 1
    else:
        menor = menor + 1
print('Das pessoas digitadas, {} são MAIORES de idade, e {} são MENORES !!!'.format(maior, menor))