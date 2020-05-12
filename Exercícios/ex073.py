tabela = ('Santos', 'Palmeiras', 'Flamengo', 'Atlético', 'São Paulo', 'Internacional', 'Corinthians',
          'Atlético-PR', 'Botafogo', 'Bahia', 'Ceará SC', 'Goiás', 'Grêmio', 'Fortaleza', 'Vasco da Gama',
          'Fluminense', 'Chapecoense', 'Cruzeiro','CSA', 'Avaí')

primeiros = tabela[0:5]
ultimos = tabela[-4:]
ordem = sorted(tabela)
posicaochape = tabela.index('Chapecoense') + 1
print(f'Os times são {tabela}')
print(f'Os cinco primeiros colocados são: {primeiros}')
print(f'Os 4 últimos são: {ultimos}')
print(f'Times em ordem alfabética: {ordem}')
print(f'A chapecoense está na {posicaochape}ª posição')