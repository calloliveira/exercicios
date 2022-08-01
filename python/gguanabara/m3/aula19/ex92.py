from datetime import date
hoje = date.today().year
funcionario = dict()
residual = 0
funcionario["Nome"] = str(input('Digite o nome: '))
funcionario["Nascimento"] = int(input('Digite o ano de nascimento: '))
funcionario["Idade"] = hoje - funcionario["Nascimento"]
funcionario["Ctps"] = int(input('Digite o Nº da CTPS (0 não tem): '))
if funcionario["Ctps"] != 0:
    funcionario["Ano_Contratacao"] = int(input('Qual o ano de contratação? '))
    funcionario["Salário"] = float(input("Qual o salário? "))
    residual = hoje - funcionario["Ano_Contratacao"]
    if residual < 35:
        faltante = 35 - residual
        funcionario["Idade_Aposentadoria"] = funcionario["Idade"] + faltante
print('=-' * 30)
print(f'{"DADOS DO TRABALHADOR":=^50}')
print('=-' * 30)
for k, v in funcionario.items():
    print(f'{k}: {v}')