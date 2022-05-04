tabela = ('Santos', 'Atlético-MG', 'Corinthians', 'Cuiabá', 'Internacional', 'Avaí', 'Bragantino', 
          'Palmeiras', 'Flamengo', 'Coritiba', 'São Paulo', 'Botafogo', 
          'Fluminense', 'América-MG', 'Ceará', 'Athletico-PR', 'Atlético-GO', 'Goiás', 'Juventude', 'Fortaleza')
print('=-' * 30)
print(f'Lista de times do brasileirão: {tabela}')
print('=-' * 30)
print(f'5 primeiros colocados: {tabela[0:5]}')
print('=-' * 30)
print(f'4 últimos colocados: {tabela[-4:]}')
print('=-' * 30)
print(f'Times em ordem alfabética {sorted(tabela)}')
print('=-' * 30)
print(f'Lugar do SPFC na tabela: {tabela.index("São Paulo")+1}º')