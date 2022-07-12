from datetime import date
hoje = date.today().year
funcionario = dict()
residual = 0
funcionario["Nome"] = str(input('Digite o nome: '))
funcionario["Nascimento"] = int(input('Digite o ano de nascimento: '))
funcionario["Idade"] = hoje - funcionario["Nascimento"]
funcionario["Ctps"] = int(input('Digite o Nº da CTPS: '))
if funcionario["Ctps"] != 0:
    funcionario["Ano_Contratacao"] = int(input('Qual o ano de contratação? '))
    funcionario["Salário"] = float(input("Qual o salário atual? "))
    residual = hoje - funcionario["Ano_Contratacao"]
    if residual < 30:
        faltante = 30 - residual
        funcionario["Idade_Aposentadoria"] = funcionario["Idade"] + faltante
for k, v in funcionario.items():
    print(f'{k}: {v}')